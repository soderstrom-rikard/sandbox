// Standard C++ headers
#include <iostream>
#include <limits>

// SDL libraries
#include "SDL.h"
#include "SDL_image.h"
#include "SDL_ttf.h"

// Project headers
#include "elements.h"

/* XPM */
constexpr const char * icon_xpm[] =
{
  "32 23 3 1",
  "     c #FFFFFF",
  ".    c #000000",
  "+    c #FFFF00",
  "                                ",
  "            ........            ",
  "          ..++++++++..          ",
  "         .++++++++++++.         ",
  "        .++++++++++++++.        ",
  "       .++++++++++++++++.       ",
  "      .++++++++++++++++++.      ",
  "      .+++....++++....+++.      ",
  "     .++++.. .++++.. .++++.     ",
  "     .++++....++++....++++.     ",
  "     .++++++++++++++++++++.     ",
  "     .++++++++++++++++++++.     ",
  "     .+++++++++..+++++++++.     ",
  "     .+++++++++..+++++++++.     ",
  "     .++++++++++++++++++++.     ",
  "      .++++++++++++++++++.      ",
  "      .++...++++++++...++.      ",
  "       .++............++.       ",
  "        .++..........++.        ",
  "         .+++......+++.         ",
  "          ..++++++++..          ",
  "            ........            ",
  "                                "
};

SDL_Texture* String2Texture(const SDL_Color & color, const int32_t font_size, const std::string_view &text, SDL_Renderer *renderer)
{
    if (!TTF_WasInit() && TTF_Init() == -1)
    {
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "TTF_Init() failed: %s", TTF_GetError());
        return nullptr;
    }

    TTF_Font *mono = TTF_OpenFont("/usr/share/fonts/TTF/DejaVuSansMono.ttf", font_size);
    if (mono == nullptr)
    {
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "mono_font_16 is nullptr");
        return nullptr;
    }

    SDL_Texture *texture = nullptr;
    if (SDL_Surface *surface = TTF_RenderText_Solid(mono, text.data(), color); surface != nullptr)
        texture = SDL_CreateTextureFromSurface(renderer, surface);

    if (TTF_WasInit()) TTF_Quit();

    return texture;
}

int main(int argc, char *argv[])
{
    static_cast<void>(argc);
    static_cast<void>(argv);
    SDL_Window   *window;
    SDL_Renderer *renderer;

    if (SDL_CreateWindowAndRenderer(0, 0, 0, &window, &renderer) < 0)
    {
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "SDL_CreateWindowAndRenderer() failed: %s", SDL_GetError());
        return 2;
    }

    const element_t &  chemical_element = get_element(0);

    std::cout << "element name " << chemical_element.name << std::endl;

    SDL_Texture* symbol_texture = String2Texture(SDL_Color{0,0,255,0}, 16, chemical_element.symbol, renderer);
    SDL_Texture* name_texture   = String2Texture(SDL_Color{0,0,  0,0},  8, chemical_element.name  , renderer);

    SDL_Rect symbol_rect = {20, 20, 50, 50};
    SDL_Rect name_rect   = {10, 10, 50 , 8};

    SDL_Surface *surface = IMG_ReadXPMFromArray(const_cast<char**>(icon_xpm));
    SDL_Texture *texture = SDL_CreateTextureFromSurface(renderer, surface);
    if (!texture)
    {
      SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Couldn't load texture: %s", SDL_GetError());
      return 2;
    }
    SDL_SetWindowSize(window, 800, 480);

    bool running = true;
    while (running)
    {
        SDL_Event event;
        while (SDL_PollEvent(&event))
        {
            if (event.type == SDL_QUIT) running = false;
        }

        SDL_RenderCopy(renderer, texture, nullptr, nullptr);
        SDL_RenderCopy(renderer, symbol_texture, nullptr, &symbol_rect);
        SDL_RenderCopy(renderer, name_texture  , nullptr, &name_rect);
        SDL_RenderPresent(renderer);
        SDL_Delay(100);
    }

    if (TTF_WasInit()) TTF_Quit();
    SDL_DestroyTexture(texture);
    SDL_Quit();

    return 0;
}

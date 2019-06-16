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

struct element_textures_t
{
    SDL_Texture * texture_atomic_number;
    SDL_Texture * texture_symbol;
    SDL_Texture * texture_name;
    SDL_Texture * texture_atomic_weight;
    SDL_Texture * texture_phase;
    SDL_Texture * texture_category;
    SDL_Texture * texture_occurrence;

    SDL_Rect rect_atomic_number;
    SDL_Rect rect_symbol;
    SDL_Rect rect_name;
    SDL_Rect rect_atomic_weight;
    SDL_Rect rect_phase;
    SDL_Rect rect_category;
    SDL_Rect rect_occurrence;
};

bool initialize_element_textures(element_textures_t & et, const element_t & element, SDL_Renderer *renderer)
{
    bool ret = true;
    if (et.texture_atomic_number = String2Texture(SDL_Color{255,255,255,255}, 16, std::to_string(element.atomic_number), renderer);et.texture_atomic_number == nullptr) ret = false;
    if (et.texture_symbol        = String2Texture(SDL_Color{  0,  0,255,  0}, 16, element.symbol                       , renderer);et.texture_symbol        == nullptr) ret = false;
    if (et.texture_name          = String2Texture(SDL_Color{  0,  0,  0,  0},  8, element.name                         , renderer);et.texture_name          == nullptr) ret = false;
    if (et.texture_atomic_weight = String2Texture(SDL_Color{255,255,255,255}, 16, std::to_string(element.atomic_weight), renderer);et.texture_atomic_weight == nullptr) ret = false;
    //if (et.texture_phase         = String2Texture(SDL_Color{255,255,255,255}, 16, std::to_string(element.phase        ), renderer);et.texture_phase         == nullptr) ret = false;
    //if (et.texture_category      = String2Texture(SDL_Color{255,255,255,255}, 16, std::to_string(element.category     ), renderer);et.texture_category      == nullptr) ret = false;
    //if (et.texture_occurrence    = String2Texture(SDL_Color{255,255,255,255}, 16, std::to_string(element.occurrence   ), renderer);et.texture_occurrence    == nullptr) ret = false;

    et.rect_atomic_number = {20,  5, 50,  8};
    et.rect_symbol        = {20, 20, 50, 50};
    et.rect_name          = {10, 10, 50,  8};
    et.rect_atomic_weight = {25, 30, 50,  8};
    et.rect_phase         = {30, 40, 50,  8};
    et.rect_category      = {40, 20, 50,  8};
    et.rect_occurrence    = {50, 40, 50,  8};

    return ret;
}

void draw_element_textures(element_textures_t & et, SDL_Renderer *renderer)
{
    SDL_RenderCopy(renderer, et.texture_atomic_number, nullptr, &et.rect_atomic_number);
    SDL_RenderCopy(renderer, et.texture_symbol       , nullptr, &et.rect_symbol       );
    SDL_RenderCopy(renderer, et.texture_name         , nullptr, &et.rect_name         );
    SDL_RenderCopy(renderer, et.texture_atomic_weight, nullptr, &et.rect_atomic_weight);
    SDL_RenderCopy(renderer, et.texture_phase        , nullptr, &et.rect_phase        );
    SDL_RenderCopy(renderer, et.texture_category     , nullptr, &et.rect_category     );
    SDL_RenderCopy(renderer, et.texture_occurrence   , nullptr, &et.rect_occurrence   );
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

    element_textures_t element_textures;
    initialize_element_textures(element_textures, chemical_element, renderer);

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
        draw_element_textures(element_textures, renderer);
        SDL_RenderPresent(renderer);
        SDL_Delay(100);
    }

    if (TTF_WasInit()) TTF_Quit();
    SDL_DestroyTexture(texture);
    SDL_Quit();

    return 0;
}

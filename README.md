# A simple save files reader for SoTF game

The reader expect one or more *.json files in the .config folder of the working director.

There are two json objects for configuration, the `input` and `output` directives.

## The `input` directives

```json
{
    "input":
    {
        "driveDir": "/path/to/Steam-compatdata-drive-c-or-windows-drive-letter",
        "savesDir": "AppData-LocalLow/Publisher/Game/Saves",
        "selectedSaveDir": "steam-id/SinglePlayer/save-id"
    }
}
```

## The `output` directives

```json
{
    "output":
    {
        "outDir": "directory-to-create-inside-working-directory-dot-config-directory",
        "overwrite": true
    }
}
```

Setting overwrite to true means that previous readouts will get overwritten

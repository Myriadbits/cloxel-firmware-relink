# Cloxel firmware – relink kit

This repository lets you rebuild the firmware of the **Cloxel** word clock, made by Myriadbits,
with your own version of the open-source libraries it uses. It is published to meet the
conditions of the GNU Lesser General Public License (LGPL) for those libraries.

The firmware is based on [WLED](https://github.com/wled/WLED) 0.15.0-b6 (MIT license).
Everything is included as source code, except the Cloxel part (the clock logic, the
letter layouts and the Bluetooth setup and update code). That part is included as a
compiled library, `precompiled/libcloxel.a`.

Firmware version in this kit: see [`VERSION`](VERSION).

## What is in the firmware

| Part | Version | License | In this kit |
| --- | --- | --- | --- |
| [WLED](https://github.com/wled/WLED), including ArduinoJson, WS2812FX and the other code in `wled00/src/dependencies` | 0.15.0-b6 with small Cloxel changes | MIT | Source |
| [FastLED](https://github.com/FastLED/FastLED) | 3.6.0 | MIT | Downloaded by PlatformIO |
| [NeoPixelBus](https://github.com/Makuna/NeoPixelBus) | 2.8.0 | LGPL-3.0 | Downloaded by PlatformIO |
| [ESPAsyncWebServer](https://github.com/Aircoookie/ESPAsyncWebServer) (WLED version) | 2.2.1 | LGPL-3.0 | Downloaded by PlatformIO |
| [AsyncTCP](https://github.com/pbolduc/AsyncTCP) | 1.2.0 | LGPL-3.0 | Downloaded by PlatformIO |
| [NimBLE-Arduino](https://github.com/h2zero/NimBLE-Arduino) | 1.4.3 | Apache-2.0 | Downloaded by PlatformIO |
| [Arduino core for the ESP32](https://github.com/espressif/arduino-esp32) | 2.0.9 | LGPL-2.1 | Downloaded by PlatformIO |
| [ESP-IDF](https://github.com/espressif/esp-idf) (inside the Arduino core) | 4.4 | Apache-2.0 | Downloaded by PlatformIO |
| Cloxel usermod | see `VERSION` | Proprietary, © Myriadbits | `precompiled/libcloxel.a` (compiled) |

The license texts are in the [`licenses`](licenses) folder. WLED's own license is in [`LICENSE`](LICENSE).

The compiled Cloxel library was built from source files that include header files of WLED and of the
libraries above, such as the ESPAsyncWebServer, AsyncTCP and NeoPixelBus headers. As required by section 3
of the LGPL-3.0: the compiled library contains material from those header files, which are covered by the
LGPL-3.0 (see `licenses/LGPL-3.0.txt` and `licenses/GPL-3.0.txt`).

## Building the firmware

1. Install [Visual Studio Code](https://code.visualstudio.com) with the
   [PlatformIO](https://platformio.org/install/ide?install=vscode) extension, or the PlatformIO command line tools,
   and [Node.js](https://nodejs.org) (used to build WLED's web interface).
2. Clone this repository and open the folder in Visual Studio Code, or run in a terminal:

   ```
   npm ci
   pio run -e wordcloxelHW1
   ```

3. The firmware is written to `.pio/build/wordcloxelHW1/firmware.bin`.

To use a changed version of one of the libraries, replace its line under `lib_deps` in
`platformio_override.ini` with your own copy, for example a folder: `lib_deps = ... file://C:/path/to/NeoPixelBus`,
or put the library in the `lib` folder and remove it from `lib_deps`. Then build again.
The library must stay compatible with the version listed above, because the compiled Cloxel library
was built against that version's header files.

## Installing the firmware on a Cloxel

The Cloxel contains an ESP32. You can install your own firmware over USB:

1. Unplug the Cloxel from the power supply.
2. Connect the USB connector on the back of the Cloxel to your computer.
3. Run `pio run -e wordcloxelHW1 -t upload`. If the upload does not start, hold the BOOT button while the upload
   begins (only needed on some boards).

Your settings (Wi-Fi, colors) are kept, because the file system is not overwritten.
Installing your own firmware is at your own risk. To go back to the official firmware, update the Cloxel
from the Cloxel app.

## Questions

Questions about this kit or the Cloxel: see [cloxel.nl/contact](https://cloxel.nl/contact/).

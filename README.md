# ovos-i2c-detection

This repo holds auto-detection scripts for I2C devices used by OpenVoiceOS.
Each function probes the I2C bus (or a serial port, for the Mark 1) and returns
`True` or `False` for the presence of a specific device.

## Install

```bash
pip install ovos-i2c-detection
```

## Usage

```python
from ovos_i2c_detection import is_sj201_v6, is_wm8960, is_mark_1

if is_sj201_v6():
    print("sj201 v6 dev kit detected")
```

The package provides these detection functions:

* Mycroft sj201 sound card
  * `is_sj201_v6` - v6 dev kit
  * `is_sj201_v10` - v10 production unit
* `is_texas_tas5806` - Texas Instruments TAS5806 audio amp (used for sj201_v10 detection)
* `is_wm8960` - WM8960 devices, including the ReSpeaker 2mic and the Adafruit 2mic
* `is_respeaker_4mic` - ReSpeaker 4mic
* `is_respeaker_6mic` - ReSpeaker 6mic
* `is_adafruit_amp` - [Adafruit audio amp](https://www.adafruit.com/product/1752)
* `is_mark_1` - Mycroft Mark 1 device
* `is_hifiberry_dac_pro` - [HiFiBerry DAC Pro](https://www.hifiberry.com/shop/boards/dac2-pro/)

## Related projects

* [OpenVoiceOS/ovos-PHAL](https://github.com/OpenVoiceOS/ovos-PHAL) - hardware abstraction layer that uses this package for device detection
* [OpenVoiceOS/ovos-PHAL-plugin-mk1](https://github.com/OpenVoiceOS/ovos-PHAL-plugin-mk1) - Mark 1 enclosure plugin
* [OpenVoiceOS/ovos-PHAL-plugin-dotstar](https://github.com/OpenVoiceOS/ovos-PHAL-plugin-dotstar) - DotStar LED plugin
* [OpenVoiceOS/ovos-PHAL-plugin-mk2-v6-fan-control](https://github.com/OpenVoiceOS/ovos-PHAL-plugin-mk2-v6-fan-control) - Mark 2 v6 fan control plugin
* [OpenVoiceOS/ovos-skill-mark1-ctrl](https://github.com/OpenVoiceOS/ovos-skill-mark1-ctrl) - Mark 1 control skill

## License

[MIT](LICENSE)

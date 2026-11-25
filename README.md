# ROK_EMG_acquisition

Python implementation of TCP-based EMG and IMU data acquisition for a SyncStation-style device, including:

- TCP socket communication
- CRC-8 command checksums
- Binary packet decoding
- CSV data storage

## Usage

Install dependencies with `pip install -r requirements.txt`.

Run `python demo.py` for an offline example using synthetic packet data.

`main.py` contains the original hardware acquisition workflow. Configure the device address using the `EMG_HOST` environment variable and verify the channel count, sampling rate, packet format, and control commands before connecting. The original receive function does not guarantee complete TCP frames. Hardware operation has not been validated in this draft.

## Citation and Acknowledgment

If you use or adapt this code for research or software development, please acknowledge its use by citing this repository.

Citation information is available via the "Cite this repository" option on GitHub.

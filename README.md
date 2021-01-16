# DuoPair Bluetooth 💙🔹
A script-based tool to enable bluetooth devices pair easily on an Dual Boot (Multi-Boot) machine. 

## ⚠️ Disclaimer

> DuoPair Bluetooth contains scripts accessing and modifying system configuaration files on your Windows / Linux. It may **risk** damaging your machine. I will not take any responsibility and would recommend you to execute at your own risk.

## ⚡ Dependencies
- Python 3.7 +
- Bash Shell (Linux)
- Powershell (Windows)

## 🧪 Tested Environment
I have used DuoPair for pairing Bluetooth Headphone with my own laptop (Asus Zephyrus G14) running **Windows 10** and **Pop OS 20.10** (Dual Boot).

Feel free to create a issue if you would any trouble running this tool. I will try to solve it for you.

## 👨‍🏫 Instructions
1. First pair your bluetooth device with your machine booted in Linux and then boot into Windows, pair your bluetooth with your system again.
2. Download [DuoPair](https://github.com/arunpandian7/dual-boot-bluetooth-pair/releases) into any one of your Windows Partition. (Assuming your Linux Distro alows you to access Windows Partitions from it)
> My recommendation is to have DuoPair in an flash drive which you can access from both the systems without an hussle.
3. Open the DuoPair folder in *File Explorer* and right click on **getBTKey.ps1** and select **Run with Powershell** from the Context Menu
4. Kindly select *Yes* in the Prompt to give User Admin Access for the script to run and fetch keys.
5. Now you will have your **BTKey.reg** file in C:\ drive. Copy that to your DuoPair Directory.
6. Boot into Linux now and open terminal in DuoPair Directory.
7. Run python file duopair.py

```shell
python3 duopair.py --reg-path [Path to BTKey.reg file]
```
8. Follow the script prompts and you will now changed the bluetooth key pair in Linux
9. Execute `sudo systemctl restart bluetooth` to restart your system bluetooth in Linux.

Now you will enjoy connecting your Bluetooth Device to your Dual Booted Machine hasslefree.

## Acknowledgement
I owe it to Mark Winterbottom's [Original Project](https://github.com/LondonAppDev/dual-boot-bluetooth-pair) for the idea and his solution which helped to achieve it. 

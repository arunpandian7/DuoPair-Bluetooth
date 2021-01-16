import configparser
import argparse
import os


def _parse_args():
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--reg_path', help='Path to reg file.', default='keys.reg')

    return parser.parse_args()


def _open_reg_file(file_path):
    """ Open file at given path and return as config option."""
    config = configparser.ConfigParser()
    config.read_file(open(file_path))

    return config


def _insert_mac_colons(mac):
    """ Bluetooth Mac directory file name."""
    if mac != "masterirk":
        mac = mac.upper()
        mac_parts = [mac[i:i + 2] for i in range(0, len(mac), 2)]
        # import pdb; pdb.set_trace()
        return ':'.join(mac_parts)
    else:
        return None


def _bluetooth_dir_name(section_name):
    """ Return the bluetooth directory name."""
    full_path = section_name.split('\\')
    last_two_macs = full_path[-1:]
    path_parts = []
    for mac in last_two_macs:
        path_parts.append(_insert_mac_colons(mac))
    print(path_parts)
    return '/'.join(path_parts)

def _process_key(key):
    """ Returns Valid Key value after removing cluters"""
    key = key.replace("hex:", "")
    key = key.replace(',',"")
    return key.upper()
def _get_info(adapter, device):
    device = _insert_mac_colons(device)
    os.system(f'./get_info.sh {adapter} {device}')
    info_parser = configparser.ConfigParser()
    info_parser.read_file(open(f'{device}.config'))
    if not info_parser.sections() == []:
        device_name = info_parser['General']['Name']
        key = info_parser['LinkKey']['Key']
        return device_name, key

def _print_info(name, key):
    print("Device Name :", name)
    print("Linux Key (To Replace) :", key)


def _process_reg_file(config):
    """ Process the reg file."""
    sections = config.sections()

    for section in sections:
        if len(section) > 72:
            print('\n')
            bt_adapter = _bluetooth_dir_name(section)
            print('BT Adapter Directory: /var/lib/bluetooth/{}'.format(bt_adapter))
            print('Paired Devices:')
            devices = [device for device in config[section]]
            for device in devices:
                if device != 'masterirk':
                    try:
                        name, old_key = _get_info(bt_adapter, device)
                        print("Device MAC:", _insert_mac_colons(device))
                        _print_info(name, old_key)
                        new_key = config[section][device]
                        print(f'New Key (Replace With) : {_process_key(new_key)}')
                    except:
                        continue


def main():
    """ Main entrypoint to script. """
    args = _parse_args()
    config = _open_reg_file(args.reg_path)
    _process_reg_file(config)


if __name__ == '__main__':
    main()


# reg_str = reg_file_to_str('/home/mark/Desktop/BTKeys.reg')
# file_path_to_dict(reg_str)



# Print

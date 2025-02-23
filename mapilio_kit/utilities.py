import subprocess
from typing import Dict, Union

from collections import ChainMap

__RULES__ = [{('HERO7', 'Wide', '4:3', None): 122.6}, {('HERO7', 'Wide ', '16:9', None): 118.2},
             {('HERO7', 'Wide', '4:3', None, 'zoom'): 64.6}, {('HERO7', 'Wide', '16:9', None, 'zoom'): 62.2},
             {('HERO7', 'Linear', '4:3', None, None): 86.0}, {('HERO7', 'Linear', '4:3', 'on', None): 86.7},
             {('HERO7', 'Linear', '4:3', None, 'zoom'): 50.0}, {('HERO7', 'Linear', '4:3', 'on', None): 51.0},
             {('HERO7', 'Linear', '16:9', None, None): 85.8}, {('HERO7', 'Linear', '16:9', 'on', None): 87.6},
             {('HERO7', 'Linear', '16:9', None, 'zoom'): 50.0}, {('HERO7', 'Linear', '16:9', 'on', 'zoom'): 51.0},
             {('HERO8', 'Wide', '4:3', None, None): 122.6}, {('HERO8', 'Wide', '16:9', None, None): 118.2},
             {('HERO8', 'Wide', '4:3', None, 'zoom'): 64.6}, {('HERO8', 'Wide', '16:9', None, 'zoom'): 62.2},
             {('HERO8', 'Linear', '4:3', None, None): 86.0}, {('HERO8', 'Linear', '4:3', 'on', None): 86.7},
             {('HERO8', 'Linear', '4:3', None, 'zoom'): 50.0}, {('HERO8', 'Linear', '4:3', 'on', 'zoom'): 51.0},
             {('HERO8', 'Narrow', '4:3', None, None): 68.0}, {('HERO8', 'Unknown (X)', '16:9', None, None): 122.6},
             {('HERO8', 'Linear', '16:9', None, None): 85.8}, {('HERO8', 'Linear', '16:9', 'on', None): 87.6},
             {('HERO8', 'Linear', '16:9', None, 'zoom'): 50.0}, {('HERO8', 'Linear', '16:9', 'on', 'zoom'): 51.0},
             {('HERO8', 'Narrow', '16:9', None, None): 68.0}, {('HERO9 Black', 'Wide', '4:3', 'boost', None): 92.0},
             {('HERO9 Black', 'Wide', '4:3', 'on', None): 113.0}, {('HERO9 Black', 'Wide', '4:3', None, None): 122.0},
             {('HERO9 Black', 'Linear', '4:3', 'boost', None): 75.0},
             {('HERO9 Black', 'Linear', '4:3', 'on', None): 87.0},
             {('HERO9 Black', 'Linear', '4:3', None, None): 92.0},
             {('HERO9 Black', 'Linear+HL', '4:3', 'boost', None): 75.0},
             {('HERO9 Black', 'Linear+HL', '4:3', 'on', None): 87.0},
             {('HERO9 Black', 'Narrow', '4:3', 'boost', None): 67.0},
             {('HERO9 Black', 'Narrow', '4:3', None, None): 73.0},
             {('HERO9 Black', 'Unknown (X)', '16:9', 'boost', None): 99.0},
             {('HERO9 Black', 'Unknown (X)', '16:9', 'on', None): 113.0},
             {('HERO9 Black', 'Unknown (X)', '16:9', None, None): 121.0},
             {('HERO9 Black', 'Wide', '16:9', 'boost', None): 92.0},
             {('HERO9 Black', 'Wide', '16:9', 'high', None): 109.0},
             {('HERO9 Black', 'Wide', '16:9', 'on', None): 109.0}, {('HERO9 Black', 'Wide', '16:9', None, None): 118.0},
             {('HERO9 Black', 'Linear', '16:9', 'boost', None): 75.0},
             {('HERO9 Black', 'Linear', '16:9', 'high', None): 87.0},
             {('HERO9 Black', 'Linear', '16:9', 'on', None): 87.0},
             {('HERO9 Black', 'Linear', '16:9', None, None): 92.0},
             {('HERO9 Black', 'Linear+HL', '16.9', 'boost', None): 75.0},
             {('HERO9 Black', 'Linear+HL', '16.9', 'on', None): 87.0},
             {('HERO9 Black', 'Linear+HL', '16.9', 'high', None): 87.0},
             {('HERO9 Black', 'Narrow', '16.9', 'boost', None): 67.0},
             {('HERO9 Black', 'Narrow', '16.9', None, None): 73.0},
             {('GoPro Max', 'Unknown (X)', '4:3', None, None): 148.8},
             {('GoPro Max', 'Wide', '4:3', None, None): 122.6}, {('GoPro Max', 'Linear', '4:3', None, None): 86.0},
             {('GoPro Max', 'Narrow', '4:3', None, None): 68.0},
             {('GoPro Max', 'Unknown (X)', '4:3', None, None): 148.8},
             {('GoPro Max', 'Wide', '4:3', None, None): 122.6}, {('GoPro Max', 'Linear', '4:3', None, None): 86.0},
             {('GoPro Max', 'Narrow', '4:3', None, None): 68.0}, {('GOPRO', 'Unknown (X)', '4:3', None, None): 94.0},
             {('GOPRO', 'Unknown (X)', '16:9', None, None): 121.0},
             {('GOPRO', 'Super View', '169:95', None, None): 121.0}]


def find_fov2(model, mode, asp_rat):
    result = ChainMap(*__RULES__)
    return result[(model, mode, asp_rat)]


def calculate_aspect_ratio(image_size: str) -> str:
    """

    Args:
        image_size: "1920x1080" format

    Returns:
        "16:9"
    """
    width, height = int(image_size.split("x")[0]), int(image_size.split("x")[1]),

    def gcd(a, b):
        """En büyük ortak böleni bulan fonksiyon"""
        return a if b == 0 else gcd(b, a % b)

    r = gcd(width, height)
    x = int(width / r)
    y = int(height / r)

    return f"{x}:{y}"


def get_exiftool_specific_feature(video_or_image_path: str) -> Dict[str, Union[None, str, float]]:
    """

    Args:
        video_or_image_path:

    Returns:

    """
    process = subprocess.Popen(["exiftool", video_or_image_path], stdout=subprocess.PIPE)
    dict_object = {
        'field_of_view': None,
        'device_make': None,
        'device_model': None,
        'image_size': None
    }
    fov_str = None
    fov_deg = None
    while True:
        try:
            line = process.stdout.readline()
            filtered_line = line.rstrip().decode('utf-8')
            if not line: # noqa
                break
            if 'Field Of View' in filtered_line:
                fov_str = filtered_line.split(':')[1].lstrip(' ')
                dict_object['field_of_view'] = fov_str
            elif 'Camera Elevation Angle' in filtered_line:
                fov_deg = float(filtered_line.split(':')[1].lstrip(' '))
            if 'Color Mode' in filtered_line:
                dict_object['device_make'] = filtered_line.split(':')[1].lstrip(' ')
            elif 'Make' in filtered_line:
                dict_object['device_make'] = filtered_line.split(':')[1].lstrip(' ')
            if 'Camera Model Name' in filtered_line:
                dict_object['device_model'] = filtered_line.split(':')[1].lstrip(' ')
            if 'Image Size' in filtered_line:
                dict_object['image_size'] = filtered_line.split(':')[1].lstrip(' ')
        except TypeError:
            raise f"Exif data does not Exist !" \
                  f"Please remove this video file {video_or_image_path}"

    if dict_object['field_of_view'] and "deg" in dict_object['field_of_view']:
        dict_object['field_of_view'] = float(dict_object['field_of_view'].replace('deg', ''))
        return dict_object
    if isinstance(fov_deg, float):
        dict_object['field_of_view'] = fov_deg
        return dict_object
    if isinstance(fov_str, str):
        aspect_ratio = calculate_aspect_ratio(dict_object['image_size'])
        dict_object['field_of_view'] = find_fov2(dict_object['device_make'],
                                                 dict_object['field_of_view'],
                                                 aspect_ratio)
        return dict_object


def photo_uuid_generate(user_email: str, descs: list) -> list:
    """

    Args:
        user_email:
        descs: descriptions

    Returns:
        add new column as name "Id" create hash
    """
    import hashlib

    for desc in descs[:-1]:
        code = f'{user_email}--{desc["CaptureTime"]}'
        hash_object = hashlib.md5(code.encode())
        desc['PhotoUUID'] = hash_object.hexdigest()

    return descs
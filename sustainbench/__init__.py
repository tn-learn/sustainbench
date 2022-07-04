from .version import __version__
from .get_dataset import get_dataset

benchmark_datasets = [
    'poverty',
    'poverty_change_dataset',
    'fmow',
    'africa_crop_type_mapping',
    'crop_seg',
    'education',
    'crop_type_kenya',
    'crop_yield',
    'weak_cropland',
    'brick_kiln'
]

additional_datasets = [
]

supported_datasets = benchmark_datasets + additional_datasets
"""
 Copyright (c) 2022, salesforce.com, inc.
 All rights reserved.
 SPDX-License-Identifier: BSD-3-Clause
 For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
"""

import os
from pathlib import Path

from omegaconf import OmegaConf

from lavis.common.utils import (
    cleanup_dir,
    download_and_extract_archive,
    get_abs_path,
    get_cache_path,
)


# TODO
# 1. Go to https://www.mediafire.com/file/czh8sezbo9s4692/test_videos.zip/file
#      and https://www.mediafire.com/file/x3rrbe4hwp04e6w/train_val_videos.zip/file
# 2. Right-click the Download button and copy the link address
#      e.g.
#    DATA_URL = {
#        "train": "https://download1602.mediafire.com/xxxxxxxxxxxx/x3rrbe4hwp04e6w/train_val_videos.zip",
#        "test": "https://download2390.mediafire.com/xxxxxxxxxxxx/czh8sezbo9s4692/test_videos.zip",
#    }
# 3. Paste the link address to DATA_URL

DATA_URL = "https://b1.thefileditch.ch/aaJJJzuveZiHMGguKKXp.zip"


def download_datasets(root, url):
    """
    Download the Imagenet-R dataset archives and expand them
    in the folder provided as parameter
    """
    download_and_extract_archive(url=url, download_root=root)




if __name__ == "__main__":

    config_path = get_abs_path("configs/datasets/mixkit/defaults_cap.yaml")

    storage_dir = OmegaConf.load(
        config_path
    ).datasets.msrvtt_cap.build_info.videos.storage

    storage_dir = Path(get_cache_path(storage_dir))

    if storage_dir.exists():
        print(f"Dataset already exists at {storage_dir}. Aborting.")
        exit(0)

    try:
        print("Downloading {}".format(DATA_URL))
        download_datasets(storage_dir, v)
    except Exception as e:
        # remove download dir if failed
        cleanup_dir(storage_dir)
        print("Failed to download or extracting datasets. Aborting.")

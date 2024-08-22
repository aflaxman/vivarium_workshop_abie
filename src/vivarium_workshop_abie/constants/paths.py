from pathlib import Path

import vivarium_workshop_abie
from vivarium_workshop_abie.constants import metadata

BASE_DIR = Path(vivarium_workshop_abie.__file__).resolve().parent

ARTIFACT_ROOT = Path(
    f"/mnt/team/simulation_science/pub/models/{metadata.PROJECT_NAME}/artifacts/"
)

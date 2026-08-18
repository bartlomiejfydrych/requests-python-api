import os
import random as random_module
import time

from faker import Faker

# ==========================================================================================================
# FIELDS
# ==========================================================================================================

# NOTE FOR ME: Javowe "-Dtest.seed=..." (system property) -> zmienna środowiskowa TEST_SEED
_SEED_ENV_VALUE: str | None = os.environ.get("TEST_SEED")
_SEED_PROVIDED: bool = _SEED_ENV_VALUE is not None
_SEED: int = int(_SEED_ENV_VALUE) if _SEED_PROVIDED else int(time.time() * 1000)

_RANDOM: random_module.Random = random_module.Random(_SEED)

_FAKER: Faker = Faker()
_FAKER.seed_instance(_SEED)

# ==========================================================================================================
# MODULE INITIALIZATION (odpowiednik Javowego "static initialization block")
# ==========================================================================================================

print("=========================================")
print("---------")
print("TEST SEED")
print("---------")

if _SEED_PROVIDED:
    print(f"Using PROVIDED TEST_SEED = {_SEED}")
else:
    print(f"Using GENERATED TEST_SEED = {_SEED}")

print("FOR COPY:")
print(f"TEST_SEED={_SEED} pytest")
print("=========================================")
print()


# ==========================================================================================================
# METHODS – MAIN
# ==========================================================================================================

# ------
# RANDOM
# ------

def random() -> random_module.Random:
    return _RANDOM


# -----
# FAKER
# -----

def faker() -> Faker:
    return _FAKER


# --------------
# SEED IN RAPORT
# --------------

def seed() -> int:
    return _SEED

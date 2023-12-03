import json
import os
from typing import Optional

from src.main.model.vehicle import Vehicle
from src.main.config.config import config
from src.main.util.logger import logger

LOCAL_S3_PATH = os.path.join('.tmp', 's3')


class RepositoryService:


    def save_vehicle(self, vehicle: Vehicle) -> None:

        if config['backend']['env'] == 'local':
            logger.info("saving to s3, local implementation")

            if not os.path.exists(LOCAL_S3_PATH):
                os.makedirs(LOCAL_S3_PATH)

            if vehicle.licensePlate is None:
                vehicle.licensePlate = 'ABC123'

            object_path = os.path.join(LOCAL_S3_PATH, vehicle.licensePlate)
            with open(object_path, 'w') as f:
                json.dump(vehicle.dict(), f)

        
        if config['backend']['env'] == 'cloud':
            raise NotImplementedError()
        
    def get_vehicle(self, license_plate: str) -> Optional[Vehicle]:

        if config['backend']['env'] == 'local':
            logger.info("getting car from s3, local implementation")
            object_path = os.path.join(LOCAL_S3_PATH, license_plate)

            if not os.path.exists(object_path):
                logger.info("license plate %s not found in bucket", license_plate)
                return None
            
            with open(object_path, 'r') as f:
                vehicle_dict = json.load(f)
                return Vehicle(**vehicle_dict)      

        if config['backend']['env'] == 'cloud':
            raise NotImplementedError()

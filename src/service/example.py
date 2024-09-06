from loguru import logger
from py_spring.core.entities.component import Component
from py_spring.core.entities.properties.properties import Properties


class ExampleProperties(Properties):
    __key__ = "example"
    value: str

class ExampleService(Component):
    example_properties: ExampleProperties


    def post_construct(self) -> None:
        logger.info(f"Example value: {self.example_properties.value}")

    def pre_destroy(self) -> None:
        logger.info("Pre destroy method called")



class AnotherExampleService(Component):
    example_service: ExampleService

    def post_construct(self) -> None:
        logger.info("EmailNotificationService post construct called")
        logger.info(f"Example value: {self.example_service.example_properties.value}")
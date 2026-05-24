from dataclasses import dataclass


@dataclass(slots=True)
class User:
    id: int
    telegram_id: int
    username: str | None
    first_name: str | None
    created_at: str


@dataclass(slots=True)
class Project:
    id: int
    user_id: int
    marketplace: str
    category: str
    product_name: str
    product_data_json: str
    main_image_path: str | None
    result_json: str
    generated_images_json: str | None
    created_at: str
    updated_at: str

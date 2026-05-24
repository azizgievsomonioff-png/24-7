from pathlib import Path

import aiosqlite

from config import settings


SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE NOT NULL,
    username TEXT,
    first_name TEXT,
    created_at TEXT
);

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    marketplace TEXT,
    category TEXT,
    product_name TEXT,
    product_data_json TEXT,
    main_image_path TEXT,
    result_json TEXT,
    generated_images_json TEXT,
    created_at TEXT,
    updated_at TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
"""


def ensure_data_dirs() -> None:
    settings.db_path.parent.mkdir(parents=True, exist_ok=True)
    (Path(__file__).resolve().parent.parent / "data" / "projects").mkdir(parents=True, exist_ok=True)
    (Path(__file__).resolve().parent.parent / "data" / "exports").mkdir(parents=True, exist_ok=True)


async def get_connection() -> aiosqlite.Connection:
    ensure_data_dirs()
    db = await aiosqlite.connect(settings.db_path)
    db.row_factory = aiosqlite.Row
    return db


async def init_db() -> None:
    db = await get_connection()
    try:
        await db.executescript(SCHEMA)
        cursor = await db.execute("PRAGMA table_info(projects)")
        columns = {row["name"] for row in await cursor.fetchall()}
        if "generated_images_json" not in columns:
            await db.execute("ALTER TABLE projects ADD COLUMN generated_images_json TEXT")
        await db.commit()
    finally:
        await db.close()

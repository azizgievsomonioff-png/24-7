from datetime import datetime

from database.db import get_connection


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


async def upsert_user(telegram_id: int, username: str | None, first_name: str | None) -> int:
    db = await get_connection()
    try:
        await db.execute(
            """
            INSERT INTO users (telegram_id, username, first_name, created_at)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(telegram_id) DO UPDATE SET username=excluded.username, first_name=excluded.first_name
            """,
            (telegram_id, username, first_name, now_iso()),
        )
        await db.commit()
        cursor = await db.execute("SELECT id FROM users WHERE telegram_id = ?", (telegram_id,))
        row = await cursor.fetchone()
        return int(row["id"])
    finally:
        await db.close()


async def get_user_id(telegram_id: int) -> int | None:
    db = await get_connection()
    try:
        cursor = await db.execute("SELECT id FROM users WHERE telegram_id = ?", (telegram_id,))
        row = await cursor.fetchone()
        return int(row["id"]) if row else None
    finally:
        await db.close()


async def create_project(
    user_id: int,
    marketplace: str,
    category: str,
    product_name: str,
    product_data_json: str,
    main_image_path: str | None,
    result_json: str,
) -> int:
    now = now_iso()
    db = await get_connection()
    try:
        cursor = await db.execute(
            """
            INSERT INTO projects (
                user_id, marketplace, category, product_name, product_data_json,
                main_image_path, result_json, generated_images_json, created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (user_id, marketplace, category, product_name, product_data_json, main_image_path, result_json, "[]", now, now),
        )
        await db.commit()
        return int(cursor.lastrowid)
    finally:
        await db.close()


async def list_user_projects(telegram_id: int, limit: int = 10) -> list[dict]:
    db = await get_connection()
    try:
        cursor = await db.execute(
            """
            SELECT p.* FROM projects p
            JOIN users u ON u.id = p.user_id
            WHERE u.telegram_id = ?
            ORDER BY p.created_at DESC
            LIMIT ?
            """,
            (telegram_id, limit),
        )
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]
    finally:
        await db.close()


async def get_project(project_id: int, telegram_id: int) -> dict | None:
    db = await get_connection()
    try:
        cursor = await db.execute(
            """
            SELECT p.* FROM projects p
            JOIN users u ON u.id = p.user_id
            WHERE p.id = ? AND u.telegram_id = ?
            """,
            (project_id, telegram_id),
        )
        row = await cursor.fetchone()
        return dict(row) if row else None
    finally:
        await db.close()


async def delete_project(project_id: int, telegram_id: int) -> bool:
    db = await get_connection()
    try:
        cursor = await db.execute(
            """
            DELETE FROM projects
            WHERE id = ? AND user_id = (SELECT id FROM users WHERE telegram_id = ?)
            """,
            (project_id, telegram_id),
        )
        await db.commit()
        return cursor.rowcount > 0
    finally:
        await db.close()


async def update_project_images(project_id: int, telegram_id: int, generated_images_json: str) -> bool:
    db = await get_connection()
    try:
        cursor = await db.execute(
            """
            UPDATE projects
            SET generated_images_json = ?, updated_at = ?
            WHERE id = ? AND user_id = (SELECT id FROM users WHERE telegram_id = ?)
            """,
            (generated_images_json, now_iso(), project_id, telegram_id),
        )
        await db.commit()
        return cursor.rowcount > 0
    finally:
        await db.close()


async def update_project_result(project_id: int, telegram_id: int, result_json: str) -> bool:
    db = await get_connection()
    try:
        cursor = await db.execute(
            """
            UPDATE projects
            SET result_json = ?, updated_at = ?
            WHERE id = ? AND user_id = (SELECT id FROM users WHERE telegram_id = ?)
            """,
            (result_json, now_iso(), project_id, telegram_id),
        )
        await db.commit()
        return cursor.rowcount > 0
    finally:
        await db.close()

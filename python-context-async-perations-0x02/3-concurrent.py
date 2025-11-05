#!/usr/bin/env python3
import asyncio
import aiosqlite

async def async_fetch_users():
    """Fetch all users asynchronously."""
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            results = await cursor.fetchall()
            print("[ASYNC] All Users:", results)
            return results


async def async_fetch_older_users():
    """Fetch users older than 40 asynchronously."""
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            results = await cursor.fetchall()
            print("[ASYNC] Older Users (>40):", results)
            return results


async def fetch_concurrently():
    """Run both queries concurrently using asyncio.gather."""
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print("\n[SUMMARY] Concurrent Results:")
    print(results)


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())

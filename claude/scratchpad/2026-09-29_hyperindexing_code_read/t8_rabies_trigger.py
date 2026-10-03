"""T8: HyperDatabase schema's Rabies trigger names a column (first_encountered) that the words table does not have."""
import sqlite3
c=sqlite3.connect(':memory:')
c.executescript("""CREATE TABLE words (label TEXT PRIMARY KEY, payload TEXT NOT NULL, length INTEGER NOT NULL, indexed_at TEXT NOT NULL, metadata TEXT, incomplete INTEGER DEFAULT 0);
CREATE TRIGGER rabies_immutable BEFORE UPDATE OF first_encountered ON words BEGIN SELECT RAISE(ABORT,'immutable'); END;""")
c.execute("INSERT INTO words VALUES('a','p',1,'t',NULL,0)")
c.execute("UPDATE words SET indexed_at='changed' WHERE label='a'")
print("update allowed, trigger did not fire:", c.execute("select indexed_at from words").fetchone())

import os
import sqlite3 as sql

dirname = os.path.dirname(__file__)

malts_connection = sql.connect(os.path.join(dirname, "..", "data", "malts.db"))
hops_connection = sql.connect(os.path.join(dirname, "..", "data", "hops.db"))
yeasts_connection = sql.connect(
    os.path.join(dirname, "..", "data", "yeasts.db"))


def get_malts_connection():
    return malts_connection


def get_hops_connection():
    return hops_connection


def get_yeasts_connection():
    return yeasts_connection

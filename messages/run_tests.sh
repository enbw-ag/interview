#!/bin/bash

export $(cat .env)
pytest -vv .
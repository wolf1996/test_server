#!/bin/bash
uwsgi --http :9090 --mount /=test:app

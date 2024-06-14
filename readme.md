# FastAPI Addition Project

## Introduction
EY assignment for FastAPI application that provides an endpoint for performing addition on input lists of integers. This includes request and response validation using Pydantic models, implements the logic using Python's multiprocessing pool, and contains unit tests for various edge cases and scenarios.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Running the Application](#running)

## Requirements
- Python 3.8+
- FastAPI
- Pydantic
- Uvicorn
- Pytest

## Recommended Modules
- Multiprocessing for parallel processing

## Running the Application
- uvicorn app.main:app --reload
import time
import pandas
import os
import json
import random
import pandas

from datetime import datetime, timedelta, timezone
from re import match

from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
import pandas as pd
from django_pandas.io import read_frame
from django.db.models import Model 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.cache import cache
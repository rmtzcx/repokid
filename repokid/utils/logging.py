#     Copyright 2020 Netflix, Inc.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
from datetime import datetime
import json
import logging
from socket import gethostname
import traceback


class JSONFormatter(logging.Formatter):
    """Custom formatter to output log records as JSON."""

    hostname = gethostname()

    def format(self, record):
        """Format the given record into JSON."""
        message = {
            "time": datetime.utcfromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
            "process": record.process,
            "thread": record.threadName,
            "hostname": self.hostname,
            "filename": record.filename,
            "function": record.funcName,
            "lineNo": record.lineno,
        }

        if record.exc_info:
            message[
                "exception"
            ] = f"{record.exc_info[0].__name__}: {record.exc_info[1]}"
            message["traceback"] = traceback.format_exc()

        return json.dumps(message, ensure_ascii=False)

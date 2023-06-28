# Draw some gantt charts
This repository is a just a script that one can use via CLI to draw a gantt chart from a json file.

## What should my source (json) file look like?
Check out the [example.json](data/example.json) file in the data directory. It is a json file that contains two main keys.
- `Date`: Contains the date of when the current gantt chart was created. It acts as a timestamp and will also be plotted as the timeline title.
- `Tasks`: Contains a list of dictionaries. Each dictionary represents a task. The keys of the dictionary are the following:
    - `Task`: The name/description of the task
    - `Start`: The start date of the task in the format `yyyy-mm-dd`
    - `Finish`: The end date of the task in the format `yyyy-mm-dd`
    - `State`: Either "Not Started", "In Progress" or "Completed"

```json
{
    "date": "2023-06-28",
    "tasks": [
        {
            "Task": "Understand the <br>requirements and problems",
            "Start": "2023-06-14",
            "Finish": "2023-06-21",
            "State": "Completed"
        },
        ...
    ]
}
```

## How to install this?
Install via SSH (`pip install git+https://github.com/frank690/draw-some-gantts.git@main`).

## How to use this?
After installing run `draw-some-gantts --help` to see the available options.
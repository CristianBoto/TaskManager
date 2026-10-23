import json

from task_manager import TaskManager


def make_manager(tmp_path, monkeypatch):
    file_path = tmp_path / "tasks.json"
    monkeypatch.setattr(TaskManager, "FILENAME", str(file_path))
    manager = TaskManager()
    return manager, file_path


def test_add_task_creates_and_saves_new_task(tmp_path, monkeypatch):
    manager, file_path = make_manager(tmp_path, monkeypatch)

    manager.add_task("Estudiar pytest")

    assert len(manager._tasks) == 1
    assert manager._tasks[0].id == 1
    assert manager._tasks[0].description == "Estudiar pytest"
    assert manager._tasks[0].completed is False

    data = json.loads(file_path.read_text(encoding="utf-8"))
    assert data == [{"id": 1, "description": "Estudiar pytest", "completed": False}]


def test_list_tasks_prints_each_task(capsys, tmp_path, monkeypatch):
    manager, _ = make_manager(tmp_path, monkeypatch)

    manager.add_task("Leer documentación")
    manager.list_tasks()

    captured = capsys.readouterr()
    assert "Leer documentación" in captured.out
    assert "#1" in captured.out


def test_complete_task_marks_task_as_completed(tmp_path, monkeypatch):
    manager, file_path = make_manager(tmp_path, monkeypatch)

    manager.add_task("Comprar pan")
    manager.complete_task(1)

    assert manager._tasks[0].completed is True

    data = json.loads(file_path.read_text(encoding="utf-8"))
    assert data[0]["completed"] is True


def test_delete_task_removes_task_from_list_and_file(tmp_path, monkeypatch):
    manager, file_path = make_manager(tmp_path, monkeypatch)

    manager.add_task("Tarea 1")
    manager.add_task("Tarea 2")
    manager.delete_task(1)

    assert [task.id for task in manager._tasks] == [2]
    assert manager._tasks[0].description == "Tarea 2"

    data = json.loads(file_path.read_text(encoding="utf-8"))
    assert data == [{"id": 2, "description": "Tarea 2", "completed": False}]


def test_save_tasks_writes_json_to_file(tmp_path, monkeypatch):
    manager, file_path = make_manager(tmp_path, monkeypatch)

    manager.add_task("Guardar datos")
    manager.add_task("Revisar notas")

    data = json.loads(file_path.read_text(encoding="utf-8"))
    assert len(data) == 2
    assert data[0] == {"id": 1, "description": "Guardar datos", "completed": False}
    assert data[1] == {"id": 2, "description": "Revisar notas", "completed": False}


def test_load_tasks_restores_tasks_from_file(tmp_path, monkeypatch):
    file_path = tmp_path / "tasks.json"
    file_path.write_text(
        json.dumps(
            [
                {"id": 1, "description": "Tarea cargada", "completed": False},
                {"id": 2, "description": "Otra tarea", "completed": True},
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(TaskManager, "FILENAME", str(file_path))
    manager = TaskManager()

    assert len(manager._tasks) == 2
    assert [task.description for task in manager._tasks] == ["Tarea cargada", "Otra tarea"]
    assert manager._tasks[1].completed is True
    assert manager._next_id == 3

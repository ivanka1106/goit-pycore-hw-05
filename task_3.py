import sys
import os
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    """
    Парсить рядок з логу та повертає словник з розібраними компонентами.
    """
    parts = line.split(' ', 3)
    if len(parts) < 4:
        return None  #Якщо рядок не містить усіх компонентів
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path: str) -> list:
    """
    Завантажує логи з файлу.
    """
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line.strip())
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрує логи за рівнем."""
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    """Підраховує кількість записів за рівнем логування."""
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    print(f"Результат підрахунку: {counts}")
    return counts

def display_log_counts(counts: dict):
    """Виводить результати підрахунку в читабельній формі."""
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level.ljust(16)} | {count}")

def main():
    if len(sys.argv) < 2:
        print("Ви повинні вказати шлях до файлу логів.")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None
    
    logs = load_logs(file_path)
    print(f"Логи завантажені: {logs}")
    
    log_counts = count_logs_by_level(logs)
    print (f"Тип log_counts: {type(log_counts)}")
    print(log_counts)
    
    display_log_counts(log_counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs,level_filter)
        print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']}{log['time']} - {log['message']}")

if __name__ == "__main__":
    main()



#python task_3.py logfile.log


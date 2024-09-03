import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
import matplotlib.pyplot as plt
from io import BytesIO

st.title("Исследование по чаевым")

## Шаг 1. Загруска CSV файла
tips = st.sidebar.file_uploader("Загрузи CSV фаил tips.csv", type='csv')

if tips is not None:
    if tips.name == "tips.csv":
        df = pd.read_csv(tips, sep=',', index_col=0)
        number_of_rows = len(df.index)

        #создаём колонку с датами
        df["time_order"] = pd.to_datetime(np.random.choice(pd.date_range("2023-01-01", "2023-01-31"), size=number_of_rows))
        df["time_order"] = df["time_order"].dt.strftime('%Y-%m-%d')

        st.write(df.head(5))
    else:
        st.error("Загрузите файл **ТОЛЬКО** с названием '**tips.csv**'.")
        st.stop()
else:
    st.stop()

## Шаг 2. Создание графиков



### График 1
st.write("## 1. Динамика чаевых во времени")

# Создание графика
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x="tip", y="time_order", hue="size", size="size", sizes=(50, 100))
ax.set_title("Динамика чаевых во времени")
ax.set_xlabel("Чаевые")
ax.set_ylabel("Дата")
st.pyplot(fig)

# Сохранение графика PNG
buffer = BytesIO()
fig.savefig(buffer, format="png")
buffer.seek(0)

# Кнопка для скачивания графика
st.sidebar.download_button(
    label="Скачать график 1", 
    data=buffer, 
    file_name="Динамика чаевых во времени.png", 
    mime="image/png")




### График 2
st.write("## 2. Распределение общего счёта")

# Создание графика
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(x="total_bill", data=df, ax=ax)
ax.set_xlabel("Общий счёт")
ax.set_title("Распределение общего счёта")
st.pyplot(fig)

# Сохранение графика PNG
buffer = BytesIO()
fig.savefig(buffer, format="png")
buffer.seek(0)

# Кнопка для скачивания графика
st.sidebar.download_button(
    label="Скачать график 2", 
    data=buffer, 
    file_name="Распределение общего счёта.png", 
    mime="image/png")




### График 3
st.write("## 3. Связь между чаевыми и общим счётом")

# Фильтруем данные
filtered = df[(df["tip"] <= 6) & (df["total_bill"] <= 40)]

# Создание графика
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x=filtered["total_bill"], y=filtered["tip"], ax=ax)
plt.xlabel("Общий счёт")
plt.ylabel("Чаевый")
plt.title("Связь между чаевыми и общим счётом")
st.pyplot(fig)

# Сохранение графика PNG
buffer = BytesIO()
fig.savefig(buffer, format="png")
buffer.seek(0)

# Кнопка для скачивания графика
st.sidebar.download_button(
    label="Скачать график 3", 
    data=buffer, 
    file_name="Связь между чаевыми и общим счётом.png", 
    mime="image/png")




### График 4
st.write("## 4. Связь между общим счётом, чаевыми и размер чаевых")

# Создание графика
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x="total_bill", y="tip", hue="size", size="size", sizes=(50, 100), ax=ax)
ax.set_xlabel("Общий счёт")
ax.set_ylabel("Чаевые")
ax.set_title("Связь между общим счётом, чаевыми и размер чаевых")
st.pyplot(fig)

# Сохранение графика в PNG
buffer = BytesIO()
fig.savefig(buffer, format="png")
buffer.seek(0)

# Кнопка для скачивания графика
st.sidebar.download_button(
    label="Скачать график 4",
    data=buffer,
    file_name="Связь между общим счётом, чаевыми и размер чаевых.png",
    mime="image/png")




### График 5
st.write("## 5. Связь между общим счётом и днём")

# Создание графика
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, y="total_bill", x="day", ax=ax)
ax.set_xlabel("День")
ax.set_ylabel("Общий счёт")
ax.set_title("Связь между общим счётом и днём")
st.pyplot(fig)

# Сохранение графика в PNG
buffer = BytesIO()
fig.savefig(buffer, format="png")
buffer.seek(0)

# Кнопка для скачивания графика
st.sidebar.download_button(
    label="Скачать график 5",
    data=buffer,
    file_name="Связь между общим счётом и днём.png",
    mime="image/png")




### График 6
st.write("## 6. Связь между чаевыми, днём и пол")

# Создание графика
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x="tip", y="day", hue="sex", ax=ax)
ax.set_xlabel("Чаевые")
ax.set_ylabel("День")
ax.set_title("Связь между чаевыми, днём и пол")
st.pyplot(fig)

# Сохранение графика в PNG
buffer = BytesIO()
fig.savefig(buffer, format="png")
buffer.seek(0)

# Кнопка для скачивания графика
st.sidebar.download_button(
    label="Скачать график 6",
    data=buffer,
    file_name="Связь между чаевыми, днём и пол.png",
    mime="image/png")




### График 7
st.write("## 7. Связь между суммой всех счетов, день и пол")

# Создание графика
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x="day", y="total_bill", hue="time", ax=ax)
ax.set_xlabel("День")
ax.set_ylabel("Общий счёт")
ax.set_title("Связь между суммой всех счетов, день и пол")
st.pyplot(fig)

# Сохранение графика в PNG
buffer = BytesIO()
fig.savefig(buffer, format="png")
buffer.seek(0)

# Кнопка для скачивания графика
st.sidebar.download_button(
    label="Скачать график 7",
    data=buffer,
    file_name="Связь между суммой всех счетов, день и пол.png",
    mime="image/png")




### График 8
st.write("## 8. Чаевые в период обода и чаевые в период ужина")

# Создание графика
fig = plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(data=df[df["time"] == "Lunch"], x="tip")
plt.title("Чаевые в период обода")

plt.subplot(1, 2, 2)
sns.histplot(data=df[df["time"] == "Dinner"], x="tip")
plt.title("Чаевые в период ужина")
st.pyplot(fig)

# Сохранение графика в PNG
buffer = BytesIO()
fig.savefig(buffer, format="png")
buffer.seek(0)

# Кнопка для скачивания графика
st.sidebar.download_button(label="Скачать график 8",
                           data=buffer,
                           file_name="Чаевые в период обода и чаевые в период ужина.png",
                           mime="image/png")




### График 9
st.write("## 9. Общий счёт vs чаевые для (Муж) и Общий счёт vs чаевые для (Жен)")

# Создание графика
fig = plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.scatterplot(data=df[df["sex"] == "Male"], x="total_bill", y="tip", hue="smoker")
plt.title("Общий счёт vs чаевые для (Муж)")
plt.xlabel("Общий счёт")
plt.ylabel("Чаевые")

plt.subplot(1, 2, 2)
sns.scatterplot(data=df[df["sex"] == "Female"], x="total_bill", y="tip", hue="smoker")
plt.title("Общий счёт vs чаевые для (Жен)")
plt.xlabel("Общий счёт")
plt.ylabel("Чаевые")

# Отображение графика
st.pyplot(fig)

# Сохранение графика в PNG
buffer = BytesIO()
fig.savefig(buffer, format="png")
buffer.seek(0)

# Кнопка для скачивания графика
st.sidebar.download_button(
    label="Скачать график 9",
    data=buffer,
    file_name="Общий счёт vs чаевые для (Муж) и Общий счёт vs чаевые для (Жен).png",
    mime="image/png")




### График 10
st.write("## 10. Тепловая карта корреляций")

numeric_data = df.select_dtypes(include=['float64', 'int64'])

# Создание тепловой карты корреляций
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
ax.set_title("Тепловая карта корреляций")
st.pyplot(fig)

# Сохранение графика в PNG
buffer = BytesIO()
fig.savefig(buffer, format="png")
buffer.seek(0)

# Кнопка для скачивания графика
st.sidebar.download_button(
    label="Скачать график 10",
    data=buffer,
    file_name="Тепловая карта корреляций.png",
    mime="image/png"
)
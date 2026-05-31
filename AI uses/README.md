# AI Usage and Student Performance Analysis

## 📌 Overview
This project explores the relationship between the use of Artificial Intelligence (AI) tools and student academic performance. The analysis is based on a synthetic dataset that includes information on students' age, screen time, grades before and after using AI, purpose of use, and the specific AI tools used.

## 🎯 Key Questions Answered

1.  **Do younger students use AI more?**
2.  **Do AI users spend more time on screens?**
3.  **Do students who use AI improve their grades?**
4.  **Does the purpose of using AI affect grade improvement?**
5.  **Which AI tools are most used, and which are most effective?**

## 📊 Key Findings
| Question | Finding |
| :--- | :--- |
| AI usage by age | Highest at age 15 (50%), fluctuating between 25-50% across ages 14-19. |
| Screen time | AI users: 4.47h/day \| Non-users: 4.25h/day (+0.22h difference). |
| Grade improvement | Average improvement of **+9.82 points** (median +9.50). |
| Most used AI tool | **Copilot** (14 students), followed by Gemini and ChatGPT (13 each). |
| **Most effective AI tool** | **Gemini** (+10.84 points), then Copilot (+10.00), then ChatGPT (+8.62). |

## 🛠️ Tools & Libraries Used

- **Language:** Python 3
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
- **Environment:** Jupyter Notebook / VS Code
- **Version Control:** Git & GitHub

## 📁 Repository Structure
AI_Usage_analysis/
    students_ai_usage.csv      # Dataset (CC0 Public Domain)
    analysis.py                # Full analysis script
    README.md                  # This file

## 📚 Data Source & License

- **Title:** Student AI Tools vs Exam scores
- **Author:** Muneeb Muhammad Ali
- **Source:** [Kaggle - Student AI Tools vs Exam scores](https://www.kaggle.com/datasets/muneebmuhammadali/student-ai-tools-vs-exam-scores/data)
- **License:** **CC0: Public Domain** (No copyright – free to use, modify, and share)

## 🚀 How to Reproduce

1.  **Clone this repository:**
    ```bash
    git clone https://github.com/your-username/data-analysis.git
    cd data-analysis/AI_Usage_analysis
2. **Install the required libraries:**
    ``` bash
    pip install pandas numpy matplotlib seaborn
3. **Run the analysis script:**
    ``` bash
    python analysis.py
    (Alternatively, open analysis.py in VS Code and run it directly.)

All visualizations will be displayed automatically as the script executes.
## 📝 Conclusions

- **Age does not strongly predict AI usage.** Usage fluctuates between 25% and 50% across ages 14-19.
- **Screen time difference is minimal.** AI users spend only 0.22 more hours/day on screens, suggesting AI use does not drastically increase screen exposure.
- **AI tools are associated with significant grade improvement.** Students improved by nearly 10 points on average after using AI.
- **Gemini is the most effective AI tool** for grade improvement (+10.84 points on average), despite being the second most used.
- **Copilot is the most popular** (14 users) but slightly less effective (+10.00 points).
- **ChatGPT**, while widely used (13 users), shows the lowest average improvement (+8.62 points).
- This suggests that **effectiveness is not directly tied to popularity**. Students may choose tools based on factors other than academic results (e.g., ease of use, accessibility, or habit).

## 👩‍🔬 Author
Name: Carolina Caballero
Background: Physics student, aspiring Data Analyst
Contact: estudioscct@gmail.com

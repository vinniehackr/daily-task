document.addEventListener("DOMContentLoaded", () => {
    const expenseName = document.getElementById("expense-name");
    const expenseAmount = document.getElementById("expense-amount");
    const addExpenseBtn = document.getElementById("add-expense");
    const expensesList = document.getElementById("expenses");
    const searchExpense = document.getElementById("search-expense");
    const darkModeToggle = document.getElementById("toggle-dark-mode");

    let expenses = JSON.parse(localStorage.getItem("expenses")) || [];
    let darkMode = localStorage.getItem("darkMode") === "enabled";

    function applyDarkMode() {
        if (darkMode) {
            document.body.classList.add("dark-mode");
        } else {
            document.body.classList.remove("dark-mode");
        }
    }

    function toggleDarkMode() {
        darkMode = !darkMode;
        localStorage.setItem("darkMode", darkMode ? "enabled" : "disabled");
        applyDarkMode();
    }

    function renderExpenses() {
        expensesList.innerHTML = "";
        expenses.forEach((expense, index) => {
            const li = document.createElement("li");
            li.innerHTML = `${expense.name} - ₹${expense.amount} 
                <button onclick="removeExpense(${index})">❌</button>`;
            expensesList.appendChild(li);
        });
        updateChart();
        localStorage.setItem("expenses", JSON.stringify(expenses));
    }

    function addExpense() {
        const name = expenseName.value.trim();
        const amount = parseFloat(expenseAmount.value);

        if (name === "" || isNaN(amount) || amount <= 0) {
            alert("Please enter a valid name and amount.");
            return;
        }

        expenses.push({ name, amount });
        renderExpenses();
        expenseName.value = "";
        expenseAmount.value = "";
    }

    function removeExpense(index) {
        expenses.splice(index, 1);
        renderExpenses();
    }

    function filterExpenses() {
        const query = searchExpense.value.toLowerCase();
        document.querySelectorAll("#expenses li").forEach(li => {
            li.style.display = li.textContent.toLowerCase().includes(query) ? "flex" : "none";
        });
    }

    addExpenseBtn.addEventListener("click", addExpense);
    searchExpense.addEventListener("input", filterExpenses);
    darkModeToggle.addEventListener("click", toggleDarkMode);

    // Apply Dark Mode on Load
    applyDarkMode();

    // Chart.js Setup
    const ctx = document.getElementById("expense-chart").getContext("2d");
    let chart;

    function updateChart() {
        if (chart) chart.destroy();
        chart = new Chart(ctx, {
            type: "pie",
            data: {
                labels: expenses.map(e => e.name),
                datasets: [{
                    data: expenses.map(e => e.amount),
                    backgroundColor: ["#ff6384", "#36a2eb", "#ffce56", "#4bc0c0", "#9966ff"],
                }]
            }
        });
    }

    renderExpenses();
});

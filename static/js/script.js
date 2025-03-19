// // Show or hide group input field based on button clicked
// document.getElementById('personal-btn').addEventListener('click', function() {
//     document.getElementById('group-input').style.display = 'none';
// });
// document.getElementById('group-btn').addEventListener('click', function() {
//     document.getElementById('group-input').style.display = 'block';
// });

// // Handle form submission and add expense to the table
// document.getElementById('expense-form').addEventListener('submit', function(e) {
//     e.preventDefault();

//     const expenseData = {
//         name: document.getElementById('name').value,
//         amount: parseFloat(document.getElementById('amount').value),
//         date: document.getElementById('date').value,
//         category: document.getElementById('category').value,
//         is_group: document.getElementById('group-input').style.display === 'block',
//         members: document.getElementById('members') ? document.getElementById('members').value : ''
//     };

//     // Save the expense data (you can replace this with an actual backend API call)
//     addExpenseToTable(expenseData);
//     clearForm();
// });

// // Fetch and add expense data to the table
// function addExpenseToTable(expense) {
//     const row = document.createElement('tr');
//     row.innerHTML = `
//         <td>${expense.name}</td>
//         <td>${expense.amount}</td>
//         <td>${expense.date}</td>
//         <td>${expense.category}</td>
//         <td>${expense.is_group ? expense.members : '-'}</td>
//     `;
//     document.getElementById('expenses-list').appendChild(row);
// }

// // Clear the form fields after submission
// function clearForm() {
//     document.getElementById('name').value = '';
//     document.getElementById('amount').value = '';
//     document.getElementById('date').value = '';
//     document.getElementById('category').value = '';
//     document.getElementById('members').value = '';
//     document.getElementById('group-input').style.display = 'none';
// }

// // Fetch the expenses when the page loads (For example purposes, replace with actual API call)
// window.onload = function() {
//     const expenses = []; // Replace with actual data fetch
//     expenses.forEach(expense => {
//         addExpenseToTable(expense);
//     });
// };



// Function to show only the selected section
function showSection(section) {
    // Hide all sections
    document.querySelectorAll('.content-section').forEach(sec => {
        sec.style.display = 'none';
    });

    // Show the selected section
    document.getElementById(section).style.display = 'block';

    // Update active state in the sidebar
    document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
    document.querySelector(`[onclick="showSection('${section}')"]`).classList.add('active');
}

// Show the "personal" section by default when the page loads
document.addEventListener("DOMContentLoaded", function () {
    // Hide all sections initially
    document.querySelectorAll('.content-section').forEach(sec => {
        sec.style.display = 'none';
    });

    // Show the personal section
    showSection('personal'); // You can change this to any default section you want
});






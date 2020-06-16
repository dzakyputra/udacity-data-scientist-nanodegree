# Data Scientist Capstone Project

You can read the article from this [link](https://medium.com/@dzakyputra/analyzing-starbucks-offer-data-cd44d39366fd?source=friends_link&sk=b0bf48325e3fa0afef4a2cf99e350eb2).

You can check the jupyter notebook in the `Data_Scientist_Capstone_Project.ipynb` to get the full code.

---

## Introduction
For the Capstone Project, I chose the “Optimizing App Offers With Starbucks” project, which basically trying to solve the problem on how to send the offer to the right customers.

The complete step by step of my analysis are in the jupyter notebook, the medium article will show you the result of my analysis. For this project, I only focus on analyzing the “unnecessary offer” that was being sent. It is the offer that sent to the customers, and they didn’t see it, yet somehow they still completed it (the offer completed if the customers spend a certain amount of money in a certain period of time, no matter they saw the offer or not).

## Questions
These are the questions I am trying to solve:
1. How much we loss because of the “unnecessary offer”?
2. What kind of customers that often completed the offer without viewing it?
3. How is the income differentiate between customers type?

## Conclusion
Based on the analysis, there are several things we can conclude.
1. With the unplanned offer, <b>we can “loss” up to $49,032 of revenue in a month or $588,384 of revenue in a year. So the target marketing of our offer is very important and plays a huge roll</b>.
2. <b>Female customers tend to spend more than Male customers, with the average spending per transaction is $16,3 compared to $10,4 respectively</b>. Female customers also have tendency to complete the offer even without viewing it first, so we might want to be more careful in sending the offer to them.
3. In overall, customers who complete the offer without viewing the offer first have the higher average income, <b>especially in discount offer where those who complete the offer without viewing it and those who viewed it have average income $71,060 and $67,642 respectively</b>.

## Recommendation and Future Improvements
These are the things I recommend for future work based on the data analysis result:
1. We need to be more careful in sending the offer, especially the BOGO offer where it contributes $31,230 loss in this experiment. One thing we can do is to stop giving the BOGO offer to the customers with the average purchase > 2 cups per transaction, because without giving them the offer they tend to purchase > 2 cups anyway so the BOGO offer seems not to important for them.
2. Send less offer to the Female customers, especially discount offer. We can see from the data that the average spending of Female customers is $16,3. So we might want to increase the minimum spending for the offer we send to them, because it won’t make sense if we send them the offer with “difficulty” of $10, they would accomplish it anyway. So increase the minimum purchase to $20 or $25 would be better.
3. We might want to customize the “difficulty” based on the level of income for each customer, so that people with the higher income have the higher “difficulty” as well.

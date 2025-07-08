library(ggplot2)
dataset <- read.csv("regression_data.csv")   ## Tell R to read the data file

model <- lm(Salary ~ YearsExperience, data = dataset)

slope <- coef(model)[2]
intercept <- coef(model)[1]
r <- cor(dataset$YearsExperience, dataset$Salary)
pred <- predict(model)
mse <- mean((dataset$Salary - pred)^2)

print(paste("slope =", slope))
print(paste("intercept =", intercept))
print(paste("r =", r))
print(paste("MSE =", mse))

# Plot
ggplot(dataset, aes(x = YearsExperience, y = Salary)) +
  geom_point(color = "red") +
  geom_smooth(aes(x = YearsExperience, y = Salary), method = "lm", formula = y ~ x, se = FALSE, color = "green") +
  annotate("text", x = 2.51, y = max(dataset$Salary) - 0.5,
           label = paste("y =", round(slope, 2), "x +", round(intercept, 2),
                         "\nr =", round(r, 2), "\nMSE =", round(mse, 2)),
           size = 4) +
  labs(title = "Linear Fit",
       x = "Years of Experience", y = "Salary") +
  theme_minimal()

ggsave("regression_plot_r2.png")

summary(model)  ## Parameters that evaluates the fit

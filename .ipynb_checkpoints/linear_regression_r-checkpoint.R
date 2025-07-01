dataset <- read.csv("regression_data.csv")   ## Tell R to read the data file

plot(dataset$YearsExperience, dataset$Salary, col="red")  ## Make the origrinal plot without any processing

model <- lm(Salary ~ YearsExperience, data=dataset)  ## Tell R which model to fit in and how to fit dataset into model

library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$YearsExperience, y = dataset$Salary), colour = 'red') +  ## Point layer##
  geom_line(aes(x = dataset$YearsExperience, y = predict(model, newdata = dataset)), colour = 'blue') +  ## Line layer##
  ggtitle('Salary vs Experience') +
  xlab('Years of experience') +
  ylab('Salary')

summary(model)  ## Parameters that evaluates the fit

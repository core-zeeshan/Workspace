import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
X,y=make_regression(n_samples=500,n_features=10,noise=15,random_state=42)
print(f"X shape: {X.shape}, y shape: {y.shape}")


from sklearn.model_selection import train_test_split
X_train, X_test,y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print(f"Train: {X_train.shape}, Test: {X_test.shape}")



from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
print(f"Train mean: {X_train_scaled.mean(axis=0)[:3]}")
print(f"Train std:  {X_train_scaled.std(axis=0)[:3]}")


alphas = np.logspace(-4,5,50)
print(f"Alpha range: {alphas[0]:.4f} → {alphas[-1]:.0f}")
print(f"Number of candidates: {len(alphas)}")



from sklearn.linear_model import RidgeCV
ridge_cv = RidgeCV(alphas=alphas,cv=10,scoring='neg_mean_squared_error')
ridge_cv.fit(X_train_scaled,y_train)
best_alpha = ridge_cv.alpha_
print(f"Best alpha from CV 10 :{best_alpha:.6f}")




from sklearn.linear_model import Ridge
final_ridge = Ridge(alpha=best_alpha)
final_ridge.fit(X_train_scaled,y_train)
print(f"intercept:{final_ridge.intercept_:.4f}")
print(f"Coefficients (first 5): {final_ridge.coef_[:5]}")



y_pred = final_ridge.predict(X_test_scaled)
comparison = pd.DataFrame({'Actual': y_test[:5], 'Predicted': y_pred[:5]})
print(comparison)


from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

rmse = np.sqrt(mean_squared_error(y_test,y_pred))
mae = mean_absolute_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)
n, p = X_test.shape[0], X_test.shape[1]
adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

print(f"RMSE:     {rmse:.4f}")
print(f"MAE:      {mae:.4f}")
print(f"R²:       {r2:.4f}")
print(f"Adj R²:   {adj_r2:.4f}")



from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor

ols = LinearRegression()
ols.fit(X_train_scaled, y_train)
ols_pred = ols.predict(X_test_scaled)
ols_rmse = np.sqrt(mean_squared_error(y_test, ols_pred))

dummy = DummyRegressor(strategy='mean')
dummy.fit(X_train_scaled, y_train)
dummy_pred = dummy.predict(X_test_scaled)
dummy_rmse = np.sqrt(mean_squared_error(y_test, dummy_pred))

print(f"Ridge RMSE:  {rmse:.4f}")
print(f"OLS RMSE:    {ols_rmse:.4f}")
print(f"Dummy RMSE:  {dummy_rmse:.4f} (mean predictor)")




import matplotlib.pyplot as plt

residuals = y_test - y_pred

fig, axes = plt.subplots(1, 3, figsize=(16, 5))


axes[0].scatter(y_pred, residuals, alpha=0.6, edgecolors='k', linewidth=0.3)
axes[0].axhline(y=0, color='r', linestyle='--')
axes[0].set_xlabel('Fitted Values')
axes[0].set_ylabel('Residuals')
axes[0].set_title('Residuals vs Fitted')

axes[1].scatter(y_test, y_pred, alpha=0.6, edgecolors='k', linewidth=0.3)
axes[1].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
axes[1].set_xlabel('True Values')
axes[1].set_ylabel('Predicted Values')
axes[1].set_title('True vs Predicted')


axes[2].hist(residuals, bins=30, edgecolor='k', alpha=0.7)
axes[2].axvline(x=0, color='r', linestyle='--')
axes[2].set_xlabel('Residual')
axes[2].set_title('Residual Distribution')

plt.tight_layout()
plt.show()





coef_scaled = final_ridge.coef_

coef_original = coef_scaled/scaler.scale_

coef_df = pd.DataFrame({
    'Feature':[f"X{i}" for i in range(len(coef_original))],
    'coefficient scaled':coef_scaled,
    'coefficient original value': coef_original,
    'Abs Importance':np.abs(coef_original)
}).sort_values('ABs_importance',ascending=False)

print(coef_df)


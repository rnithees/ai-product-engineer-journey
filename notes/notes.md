# Day 3 — Pandas Foundation

## What I learned
- Pandas helps work with structured data like spreadsheets or SQL tables.
- A DataFrame stores rows and columns with labels.
- Unlike NumPy, Pandas keeps meaning attached to columns.

## Key Concepts
- **DataFrame** → structured table of data
- **Column thinking** → each attribute becomes a named column
- **Row filtering** → select rows using conditions
- **Feature creation** → create new columns from existing columns
- **Sorting** → reorder rows based on column values
- **describe()** → automatic statistical summary
- **apply()** → custom logic applied value-by-value
- **EDA (Exploratory Data Analysis)** → first understanding data before modeling

## Examples I practiced
- Filter rows:
  `df[df["visitors"] > 150]`

- Create new column:
  `df["weighted_score"] = df["rating"] * df["visitors"]`

- Sort values:
  `df.sort_values("rating")`

- Summary statistics:
  `df.describe()`

- Apply custom logic:
  `df["category"] = df["rating"].apply(lambda x: "High" if x > 4 else "Normal")`

## My understanding
- Filtering feels powerful because rows are selected directly without loops.
- `describe()` gives many stats because Pandas already knows numeric columns.
- `apply()` is useful when business logic is needed instead of direct math.

## Difference from NumPy
- NumPy = fast numeric operations on arrays
- Pandas = structured labeled data with analysis tools

## Keywords to remember
- DataFrame
- Filter
- Feature
- Sort
- Describe
- Apply
- EDA
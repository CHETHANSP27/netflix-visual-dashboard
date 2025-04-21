from preswald import text, connect, get_df, plotly
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 📊 Load Data
text("# Netflix Visual Insights Dashboard")
text("A visual story of Netflix trends using 10 completely different chart types.")
connect()

df = get_df("sample_csv")
df = df.dropna(subset=["release_year", "type", "country"])
df["release_year"] = df["release_year"].astype(int)

# 1️⃣ BAR CHART – Titles per Year
text("## 1. Netflix Titles Released Per Year 📊")
text("This bar chart shows how Netflix’s content has grown over the years. A clear upward trend reveals Netflix's increasing global production volume.")
year_df = df["release_year"].value_counts().sort_index().reset_index()
year_df.columns = ["Year", "Titles"]
fig1 = px.bar(year_df.tail(20), x="Year", y="Titles", title="Titles Released Per Year")
plotly(fig1)

# 2️⃣ PIE CHART – Movies vs TV Shows
text("## 2. Movies vs TV Shows 🥧")
text("This pie chart breaks down Netflix content by type. It highlights how much of the library is made up of movies versus TV series.")
type_df = df["type"].value_counts().reset_index()
type_df.columns = ["Type", "Count"]
fig2 = px.pie(type_df, names="Type", values="Count", title="Movies vs TV Shows on Netflix")
plotly(fig2)

# 3️⃣ TREEMAP – Genre Popularity
text("## 3. Genre Distribution 🌳")
text("This treemap groups Netflix titles by their first listed genre. Each block represents a genre, and the size shows how dominant that genre is.")
df = df.dropna(subset=["listed_in"])
df["genre"] = df["listed_in"].str.split(",").str[0].str.strip()
genre_df = df["genre"].value_counts().reset_index()
genre_df.columns = ["Genre", "Count"]
fig3 = px.treemap(genre_df.head(15), path=["Genre"], values="Count", title="Top Genres on Netflix (Treemap)")
plotly(fig3)

# 4️⃣ AREA CHART – Netflix Content Growth
text("## 4. Growth of Netflix Content Over Time 📈")
text("An area chart to visualize how Netflix content has grown in volume over the last two decades.")
fig4 = px.area(year_df.tail(20), x="Year", y="Titles", title="Growth of Netflix Titles Over Time")
plotly(fig4)

# 5️⃣ HISTOGRAM – Movie Duration Spread
text("## 5. Movie Duration Distribution 📏")
text("This histogram displays how long Netflix movies tend to be. Most movies fall in the 80–120 minute range, but outliers exist!")
movies = df[df["type"] == "Movie"].dropna(subset=["duration"])
movies["minutes"] = movies["duration"].str.replace(" min", "").astype(int)
fig5 = px.histogram(movies, x="minutes", nbins=20, title="Distribution of Movie Durations")
plotly(fig5)

# 6️⃣ DONUT – Content Rating Breakdown
text("## 6. Audience Ratings 🍩")
text("A donut chart showing how content is rated for different age groups — like TV-MA, PG, R, etc.")
rating_df = df["rating"].value_counts().reset_index()
rating_df.columns = ["Rating", "Count"]
fig6 = go.Figure(data=[go.Pie(labels=rating_df["Rating"], values=rating_df["Count"], hole=0.4)])
fig6.update_layout(title="Audience Rating Distribution")
plotly(fig6)

# 7️⃣ SCATTER – Director Popularity
text("## 7. Top Directors on Netflix 🎯")
text("This scatter plot shows the most frequent directors on Netflix based on the number of titles they’ve directed.")
df = df.dropna(subset=["director"])
director_df = df["director"].value_counts().reset_index()
director_df.columns = ["Director", "Count"]
fig7 = px.scatter(director_df.head(15), x="Director", y="Count", size="Count", title="Top Directors on Netflix")
plotly(fig7)

# 8️⃣ Horizontal Bar – Top Genres (as language proxy)
text("## 8. Top Global Content Themes 🌐")
text("This horizontal bar chart shows the most common Netflix genres, serving as a proxy for content type across different cultural contexts.")

genre_df_sorted = genre_df.sort_values("Count", ascending=True).tail(15)  # Use genre_df from earlier
fig8 = px.bar(genre_df_sorted, x="Count", y="Genre", orientation="h", title="Most Popular Genres Globally (Horizontal View)")
plotly(fig8)


# 9️⃣ BUBBLE – Genre Spread by Popularity
text("## 9. Genre Popularity Bubble Chart 🫧")
text("This bubble chart uses genre count to size and place each genre — bigger bubbles = more titles.")
fig9 = px.scatter(genre_df.head(15), x="Genre", y="Count", size="Count", color="Genre", title="Genre Popularity Bubble Chart")
plotly(fig9)

# 🔟 SUNBURST – Type → Rating → Genre
text("## 10. Type → Rating → Genre Hierarchy 🌞")
text("This sunburst chart maps content type to ratings to genre. It reveals how genres vary across different content types and age ratings.")
df = df.dropna(subset=["rating", "type", "genre"])
fig10 = px.sunburst(df.head(500), path=["type", "rating", "genre"], title="Content Breakdown: Type → Rating → Genre")
plotly(fig10)

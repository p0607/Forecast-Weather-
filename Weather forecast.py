{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "      <th>weather</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2012-01-01</td>\n",
       "      <td>0.0</td>\n",
       "      <td>12.8</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4.7</td>\n",
       "      <td>drizzle</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2012-01-02</td>\n",
       "      <td>10.9</td>\n",
       "      <td>10.6</td>\n",
       "      <td>2.8</td>\n",
       "      <td>4.5</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2012-01-03</td>\n",
       "      <td>0.8</td>\n",
       "      <td>11.7</td>\n",
       "      <td>7.2</td>\n",
       "      <td>2.3</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2012-01-04</td>\n",
       "      <td>20.3</td>\n",
       "      <td>12.2</td>\n",
       "      <td>5.6</td>\n",
       "      <td>4.7</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2012-01-05</td>\n",
       "      <td>1.3</td>\n",
       "      <td>8.9</td>\n",
       "      <td>2.8</td>\n",
       "      <td>6.1</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         date  precipitation  temp_max  temp_min  wind  weather\n",
       "0  2012-01-01            0.0      12.8       5.0   4.7  drizzle\n",
       "1  2012-01-02           10.9      10.6       2.8   4.5     rain\n",
       "2  2012-01-03            0.8      11.7       7.2   2.3     rain\n",
       "3  2012-01-04           20.3      12.2       5.6   4.7     rain\n",
       "4  2012-01-05            1.3       8.9       2.8   6.1     rain"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('seattle-weather.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1461, 6)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1461 entries, 0 to 1460\n",
      "Data columns (total 6 columns):\n",
      " #   Column         Non-Null Count  Dtype  \n",
      "---  ------         --------------  -----  \n",
      " 0   date           1461 non-null   object \n",
      " 1   precipitation  1461 non-null   float64\n",
      " 2   temp_max       1461 non-null   float64\n",
      " 3   temp_min       1461 non-null   float64\n",
      " 4   wind           1461 non-null   float64\n",
      " 5   weather        1461 non-null   object \n",
      "dtypes: float64(4), object(2)\n",
      "memory usage: 68.6+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: folium in c:\\users\\asus\\anaconda3\\lib\\site-packages (0.13.0)\n",
      "Requirement already satisfied: jinja2>=2.9 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from folium) (2.11.2)\n",
      "Requirement already satisfied: numpy in c:\\users\\asus\\anaconda3\\lib\\site-packages (from folium) (1.19.2)\n",
      "Requirement already satisfied: branca>=0.3.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from folium) (0.6.0)\n",
      "Requirement already satisfied: requests in c:\\users\\asus\\anaconda3\\lib\\site-packages (from folium) (2.24.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from jinja2>=2.9->folium) (1.1.1)\n",
      "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from requests->folium) (1.25.11)\n",
      "Requirement already satisfied: idna<3,>=2.5 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from requests->folium) (2.10)\n",
      "Requirement already satisfied: chardet<4,>=3.0.2 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from requests->folium) (3.0.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from requests->folium) (2020.6.20)\n",
      "Collecting geoplot\n",
      "  Downloading geoplot-0.5.1-py3-none-any.whl (28 kB)\n",
      "Requirement already satisfied: pandas in c:\\users\\asus\\anaconda3\\lib\\site-packages (from geoplot) (1.1.3)\n",
      "Collecting geopandas>=0.9.0\n",
      "  Downloading geopandas-0.12.1-py3-none-any.whl (1.1 MB)\n",
      "Collecting cartopy\n",
      "  Downloading Cartopy-0.21.0.tar.gz (10.9 MB)\n",
      "  Installing build dependencies: started\n",
      "  Installing build dependencies: still running...\n",
      "  Installing build dependencies: finished with status 'done'\n",
      "  Getting requirements to build wheel: started\n",
      "  Getting requirements to build wheel: finished with status 'done'\n",
      "    Preparing wheel metadata: started\n",
      "    Preparing wheel metadata: finished with status 'done'\n",
      "Requirement already satisfied: matplotlib>=3.1.2 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from geoplot) (3.3.2)\n",
      "Collecting mapclassify>=2.1\n",
      "  Downloading mapclassify-2.4.3-py3-none-any.whl (38 kB)\n",
      "Collecting contextily>=1.0.0\n",
      "  Downloading contextily-1.2.0-py3-none-any.whl (16 kB)\n",
      "Requirement already satisfied: seaborn in c:\\users\\asus\\anaconda3\\lib\\site-packages (from geoplot) (0.11.0)\n",
      "Requirement already satisfied: pytz>=2017.2 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from pandas->geoplot) (2020.1)\n",
      "Requirement already satisfied: numpy>=1.15.4 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from pandas->geoplot) (1.19.2)\n",
      "Requirement already satisfied: python-dateutil>=2.7.3 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from pandas->geoplot) (2.8.1)\n",
      "Requirement already satisfied: shapely>=1.7 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from geopandas>=0.9.0->geoplot) (1.7.1)\n",
      "Collecting pyproj>=2.6.1.post1\n",
      "  Downloading pyproj-3.4.0-cp38-cp38-win_amd64.whl (4.8 MB)\n",
      "Requirement already satisfied: packaging in c:\\users\\asus\\anaconda3\\lib\\site-packages (from geopandas>=0.9.0->geoplot) (20.4)\n",
      "Collecting fiona>=1.8\n",
      "  Downloading Fiona-1.8.22-cp38-cp38-win_amd64.whl (21.7 MB)\n",
      "Collecting pyshp>=2.1\n",
      "  Downloading pyshp-2.3.1-py2.py3-none-any.whl (46 kB)\n",
      "Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from matplotlib>=3.1.2->geoplot) (2.4.7)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from matplotlib>=3.1.2->geoplot) (8.0.1)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from matplotlib>=3.1.2->geoplot) (0.10.0)\n",
      "Requirement already satisfied: kiwisolver>=1.0.1 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from matplotlib>=3.1.2->geoplot) (1.3.0)\n",
      "Requirement already satisfied: certifi>=2020.06.20 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from matplotlib>=3.1.2->geoplot) (2020.6.20)\n",
      "Requirement already satisfied: scipy>=1.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from mapclassify>=2.1->geoplot) (1.5.2)\n",
      "Requirement already satisfied: networkx in c:\\users\\asus\\anaconda3\\lib\\site-packages (from mapclassify>=2.1->geoplot) (2.5)\n",
      "Requirement already satisfied: scikit-learn in c:\\users\\asus\\anaconda3\\lib\\site-packages (from mapclassify>=2.1->geoplot) (0.23.2)\n",
      "Collecting geopy\n",
      "  Downloading geopy-2.3.0-py3-none-any.whl (119 kB)\n",
      "Collecting xyzservices\n",
      "  Downloading xyzservices-2022.9.0-py3-none-any.whl (55 kB)\n",
      "Collecting rasterio\n",
      "  Downloading rasterio-1.3.4-cp38-cp38-win_amd64.whl (22.2 MB)\n",
      "Requirement already satisfied: joblib in c:\\users\\asus\\anaconda3\\lib\\site-packages (from contextily>=1.0.0->geoplot) (0.17.0)\n",
      "Requirement already satisfied: requests in c:\\users\\asus\\anaconda3\\lib\\site-packages (from contextily>=1.0.0->geoplot) (2.24.0)\n",
      "Collecting mercantile\n",
      "  Downloading mercantile-1.2.1-py3-none-any.whl (14 kB)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from python-dateutil>=2.7.3->pandas->geoplot) (1.15.0)\n",
      "Collecting cligj>=0.5\n",
      "  Downloading cligj-0.7.2-py3-none-any.whl (7.1 kB)\n",
      "Requirement already satisfied: attrs>=17 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from fiona>=1.8->geopandas>=0.9.0->geoplot) (20.3.0)\n",
      "Collecting click-plugins>=1.0\n",
      "  Downloading click_plugins-1.1.1-py2.py3-none-any.whl (7.5 kB)\n",
      "Collecting munch\n",
      "  Downloading munch-2.5.0-py2.py3-none-any.whl (10 kB)\n",
      "Requirement already satisfied: click>=4.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from fiona>=1.8->geopandas>=0.9.0->geoplot) (7.1.2)\n",
      "Requirement already satisfied: setuptools in c:\\users\\asus\\anaconda3\\lib\\site-packages (from fiona>=1.8->geopandas>=0.9.0->geoplot) (50.3.1.post20201107)\n",
      "Requirement already satisfied: decorator>=4.3.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from networkx->mapclassify>=2.1->geoplot) (4.4.2)\n",
      "Requirement already satisfied: threadpoolctl>=2.0.0 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from scikit-learn->mapclassify>=2.1->geoplot) (2.1.0)\n",
      "Collecting geographiclib<3,>=1.52\n",
      "  Downloading geographiclib-2.0-py3-none-any.whl (40 kB)\n",
      "Collecting snuggs>=1.4.1\n",
      "  Downloading snuggs-1.4.7-py3-none-any.whl (5.4 kB)\n",
      "Collecting affine\n",
      "  Downloading affine-2.3.1-py2.py3-none-any.whl (16 kB)\n",
      "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from requests->contextily>=1.0.0->geoplot) (1.25.11)\n",
      "Requirement already satisfied: idna<3,>=2.5 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from requests->contextily>=1.0.0->geoplot) (2.10)\n",
      "Requirement already satisfied: chardet<4,>=3.0.2 in c:\\users\\asus\\anaconda3\\lib\\site-packages (from requests->contextily>=1.0.0->geoplot) (3.0.4)\n",
      "Building wheels for collected packages: cartopy\n",
      "  Building wheel for cartopy (PEP 517): started\n",
      "  Building wheel for cartopy (PEP 517): finished with status 'error'\n",
      "Failed to build cartopy\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  ERROR: Command errored out with exit status 1:\n",
      "   command: 'C:\\Users\\Asus\\anaconda3\\python.exe' 'C:\\Users\\Asus\\anaconda3\\lib\\site-packages\\pip\\_vendor\\pep517\\_in_process.py' build_wheel 'C:\\Users\\Asus\\AppData\\Local\\Temp\\tmp7wl1rhhr'\n",
      "       cwd: C:\\Users\\Asus\\AppData\\Local\\Temp\\pip-install-mf2__kma\\cartopy\n",
      "  Complete output (279 lines):\n",
      "  running bdist_wheel\n",
      "  running build\n",
      "  running build_py\n",
      "  creating build\n",
      "  creating build\\lib.win-amd64-cpython-38\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\n",
      "  copying lib\\cartopy\\crs.py -> build\\lib.win-amd64-cpython-38\\cartopy\n",
      "  copying lib\\cartopy\\geodesic.py -> build\\lib.win-amd64-cpython-38\\cartopy\n",
      "  copying lib\\cartopy\\img_transform.py -> build\\lib.win-amd64-cpython-38\\cartopy\n",
      "  copying lib\\cartopy\\util.py -> build\\lib.win-amd64-cpython-38\\cartopy\n",
      "  copying lib\\cartopy\\vector_transform.py -> build\\lib.win-amd64-cpython-38\\cartopy\n",
      "  copying lib\\cartopy\\_epsg.py -> build\\lib.win-amd64-cpython-38\\cartopy\n",
      "  copying lib\\cartopy\\_version.py -> build\\lib.win-amd64-cpython-38\\cartopy\n",
      "  copying lib\\cartopy\\__init__.py -> build\\lib.win-amd64-cpython-38\\cartopy\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\feature\n",
      "  copying lib\\cartopy\\feature\\nightshade.py -> build\\lib.win-amd64-cpython-38\\cartopy\\feature\n",
      "  copying lib\\cartopy\\feature\\__init__.py -> build\\lib.win-amd64-cpython-38\\cartopy\\feature\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\io\n",
      "  copying lib\\cartopy\\io\\img_nest.py -> build\\lib.win-amd64-cpython-38\\cartopy\\io\n",
      "  copying lib\\cartopy\\io\\img_tiles.py -> build\\lib.win-amd64-cpython-38\\cartopy\\io\n",
      "  copying lib\\cartopy\\io\\ogc_clients.py -> build\\lib.win-amd64-cpython-38\\cartopy\\io\n",
      "  copying lib\\cartopy\\io\\shapereader.py -> build\\lib.win-amd64-cpython-38\\cartopy\\io\n",
      "  copying lib\\cartopy\\io\\srtm.py -> build\\lib.win-amd64-cpython-38\\cartopy\\io\n",
      "  copying lib\\cartopy\\io\\__init__.py -> build\\lib.win-amd64-cpython-38\\cartopy\\io\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\mpl\n",
      "  copying lib\\cartopy\\mpl\\clip_path.py -> build\\lib.win-amd64-cpython-38\\cartopy\\mpl\n",
      "  copying lib\\cartopy\\mpl\\contour.py -> build\\lib.win-amd64-cpython-38\\cartopy\\mpl\n",
      "  copying lib\\cartopy\\mpl\\feature_artist.py -> build\\lib.win-amd64-cpython-38\\cartopy\\mpl\n",
      "  copying lib\\cartopy\\mpl\\geoaxes.py -> build\\lib.win-amd64-cpython-38\\cartopy\\mpl\n",
      "  copying lib\\cartopy\\mpl\\geocollection.py -> build\\lib.win-amd64-cpython-38\\cartopy\\mpl\n",
      "  copying lib\\cartopy\\mpl\\gridliner.py -> build\\lib.win-amd64-cpython-38\\cartopy\\mpl\n",
      "  copying lib\\cartopy\\mpl\\patch.py -> build\\lib.win-amd64-cpython-38\\cartopy\\mpl\n",
      "  copying lib\\cartopy\\mpl\\slippy_image_artist.py -> build\\lib.win-amd64-cpython-38\\cartopy\\mpl\n",
      "  copying lib\\cartopy\\mpl\\style.py -> build\\lib.win-amd64-cpython-38\\cartopy\\mpl\n",
      "  copying lib\\cartopy\\mpl\\ticker.py -> build\\lib.win-amd64-cpython-38\\cartopy\\mpl\n",
      "  copying lib\\cartopy\\mpl\\__init__.py -> build\\lib.win-amd64-cpython-38\\cartopy\\mpl\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\conftest.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_coastline.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_coding_standards.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_crs.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_crs_transform_vectors.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_features.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_geodesic.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_img_nest.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_img_tiles.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_img_transform.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_linear_ring.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_line_string.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_polygon.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_shapereader.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_util.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\test_vector_transform.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  copying lib\\cartopy\\tests\\__init__.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\helpers.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_albers_equal_area.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_azimuthal_equidistant.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_eckert.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_equal_earth.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_equidistant_conic.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_geostationary.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_gnomonic.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_interrupted_goode_homolosine.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_lambert_azimuthal_equal_area.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_lambert_conformal.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_mercator.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_miller.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_mollweide.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_nearside_perspective.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_orthographic.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_robinson.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_rotated_geodetic.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_rotated_pole.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_sinusoidal.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_stereographic.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_transverse_mercator.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\test_utm.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  copying lib\\cartopy\\tests\\crs\\__init__.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\crs\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\feature\n",
      "  copying lib\\cartopy\\tests\\feature\\test_nightshade.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\feature\n",
      "  copying lib\\cartopy\\tests\\feature\\__init__.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\feature\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\io\n",
      "  copying lib\\cartopy\\tests\\io\\test_downloaders.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\io\n",
      "  copying lib\\cartopy\\tests\\io\\test_ogc_clients.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\io\n",
      "  copying lib\\cartopy\\tests\\io\\test_srtm.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\io\n",
      "  copying lib\\cartopy\\tests\\io\\__init__.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\io\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\conftest.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_axes.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_caching.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_contour.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_crs.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_examples.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_features.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_feature_artist.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_gridliner.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_images.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_img_transform.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_mpl_integration.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_nightshade.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_patch.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_plots.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_pseudo_color.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_quiver.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_set_extent.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_shapely_to_mpl.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_style.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_ticker.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_ticks.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\test_web_services.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\__init__.py -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_axes\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_axes\\geoaxes_set_boundary_clipping.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_axes\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_axes\\geoaxes_subslice.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_axes\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_crs\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_crs\\igh_land.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_crs\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_crs\\igh_ocean.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_crs\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_crs\\lambert_conformal_south.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_crs\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_examples\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_examples\\contour_label.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_examples\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_examples\\global_map.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_examples\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_features\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_features\\gshhs_coastlines.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_features\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_features\\natural_earth.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_features\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_features\\natural_earth_custom.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_features\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_features\\wfs.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_features\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\gridliner1.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\gridliner_labels.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\gridliner_labels_bbox_style.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\gridliner_labels_tight.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_AlbersEqualArea.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_AzimuthalEquidistant.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_EuroPP.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_Geostationary.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_Gnomonic.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_InterruptedGoodeHomolosine.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_LambertAzimuthalEqualArea.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_LambertConformal.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_LambertCylindrical.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_Mercator.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_Miller.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_Mollweide.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_NearsidePerspective.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_NorthPolarStereo.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_Orthographic.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_OSGB.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_OSNI.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_PlateCarree.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_Robinson.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_RotatedPole.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_Sinusoidal.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_SouthPolarStereo.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_Stereographic.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_AlbersEqualArea.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_AzimuthalEquidistant.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_Geostationary.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_Gnomonic.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_InterruptedGoodeHomolosine.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_LambertAzimuthalEqualArea.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_LambertConformal.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_LambertCylindrical.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_Mercator.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_Miller.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_Mollweide.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_NearsidePerspective.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_NorthPolarStereo.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_Orthographic.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_PlateCarree.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_Robinson.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_RotatedPole.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_Sinusoidal.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_SouthPolarStereo.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\\test_grid_labels_inline_usa_Stereographic.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_gridliner\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_images\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_images\\image_merge.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_images\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_images\\image_nest.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_images\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_images\\imshow_natural_earth_ortho.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_images\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_images\\imshow_regional_projected.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_images\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_images\\web_tiles.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_images\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_img_tiles2\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_img_tiles2\\web_tiles.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_img_tiles2\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_img_transform\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_img_transform\\regrid_image.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_img_transform\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\barbs_1d.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\barbs_1d_transformed.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\barbs_plate_carree.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\barbs_regrid.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\barbs_regrid_with_extent.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\global_contourf_wrap.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\global_contour_wrap.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\global_hexbin_wrap.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\global_pcolor_wrap.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\global_scatter_wrap.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\pcolormesh_global_wrap1.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\pcolormesh_global_wrap2.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\pcolormesh_global_wrap3.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\pcolormesh_goode_wrap.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\pcolormesh_limited_area_wrap.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\pcolormesh_mercator_wrap.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\pcolormesh_single_column_wrap.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\quiver_plate_carree.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\quiver_regrid.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\quiver_regrid_with_extent.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\quiver_rotated_pole.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\simple_global.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\streamplot.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_annotate.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_EckertI.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_EckertII.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_EckertIII.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_EckertIV.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_EckertV.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_EckertVI.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_EqualEarth.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_Gnomonic.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_InterruptedGoodeHomolosine.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_LambertCylindrical.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_Mercator.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_Miller.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_Mollweide.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_NorthPolarStereo.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_Orthographic.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_OSGB.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_PlateCarree.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_Robinson.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_RotatedPole.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_SouthPolarStereo.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_Stereographic.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\\test_global_map_TransverseMercator.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_mpl_integration\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_nightshade\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_nightshade\\nightshade_platecarree.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_nightshade\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_shapely_to_mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_shapely_to_mpl\\contour_with_interiors.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_shapely_to_mpl\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_shapely_to_mpl\\poly_interiors.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_shapely_to_mpl\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_ticks\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_ticks\\xticks_cylindrical.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_ticks\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_ticks\\xticks_no_transform.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_ticks\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_ticks\\xyticks.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_ticks\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_ticks\\yticks_cylindrical.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_ticks\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_ticks\\yticks_no_transform.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_ticks\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_web_services\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_web_services\\wms.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_web_services\n",
      "  copying lib\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_web_services\\wmts.png -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\mpl\\baseline_images\\mpl\\test_web_services\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: imageio in c:\\users\\asus\\anaconda3\\lib\\site-packages (2.9.0)\n",
      "Requirement already satisfied: numpy in c:\\users\\asus\\anaconda3\\lib\\site-packages (from imageio) (1.19.2)\n",
      "Requirement already satisfied: pillow in c:\\users\\asus\\anaconda3\\lib\\site-packages (from imageio) (8.0.1)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\data\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\data\\raster\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\data\\raster\\natural_earth\n",
      "  copying lib\\cartopy\\data\\raster\\natural_earth\\50-natural-earth-1-downsampled.png -> build\\lib.win-amd64-cpython-38\\cartopy\\data\\raster\\natural_earth\n",
      "  copying lib\\cartopy\\data\\raster\\natural_earth\\images.json -> build\\lib.win-amd64-cpython-38\\cartopy\\data\\raster\\natural_earth\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\data\\raster\\sample\n",
      "  copying lib\\cartopy\\data\\raster\\sample\\Miriam.A2012270.2050.2km.jpg -> build\\lib.win-amd64-cpython-38\\cartopy\\data\\raster\\sample\n",
      "  copying lib\\cartopy\\data\\raster\\sample\\Miriam.A2012270.2050.2km.README.txt -> build\\lib.win-amd64-cpython-38\\cartopy\\data\\raster\\sample\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\data\\netcdf\n",
      "  copying lib\\cartopy\\data\\netcdf\\HadISST1_SST_update.nc -> build\\lib.win-amd64-cpython-38\\cartopy\\data\\netcdf\n",
      "  copying lib\\cartopy\\data\\netcdf\\HadISST1_SST_update.README.txt -> build\\lib.win-amd64-cpython-38\\cartopy\\data\\netcdf\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\data\\shapefiles\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\data\\shapefiles\\gshhs\n",
      "  copying lib\\cartopy\\data\\shapefiles\\gshhs\\README.TXT -> build\\lib.win-amd64-cpython-38\\cartopy\\data\\shapefiles\\gshhs\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\data\\shapefiles\\gshhs\\c\n",
      "  copying lib\\cartopy\\data\\shapefiles\\gshhs\\c\\GSHHS_c_L1.dbf -> build\\lib.win-amd64-cpython-38\\cartopy\\data\\shapefiles\\gshhs\\c\n",
      "  copying lib\\cartopy\\data\\shapefiles\\gshhs\\c\\GSHHS_c_L1.shp -> build\\lib.win-amd64-cpython-38\\cartopy\\data\\shapefiles\\gshhs\\c\n",
      "  copying lib\\cartopy\\data\\shapefiles\\gshhs\\c\\GSHHS_c_L1.shx -> build\\lib.win-amd64-cpython-38\\cartopy\\data\\shapefiles\\gshhs\\c\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\data\\shapefiles\\gshhs\\l\n",
      "  copying lib\\cartopy\\data\\shapefiles\\gshhs\\l\\GSHHS_l_L2.dbf -> build\\lib.win-amd64-cpython-38\\cartopy\\data\\shapefiles\\gshhs\\l\n",
      "  copying lib\\cartopy\\data\\shapefiles\\gshhs\\l\\GSHHS_l_L2.shp -> build\\lib.win-amd64-cpython-38\\cartopy\\data\\shapefiles\\gshhs\\l\n",
      "  copying lib\\cartopy\\data\\shapefiles\\gshhs\\l\\GSHHS_l_L2.shx -> build\\lib.win-amd64-cpython-38\\cartopy\\data\\shapefiles\\gshhs\\l\n",
      "  creating build\\lib.win-amd64-cpython-38\\cartopy\\tests\\lakes_shapefile\n",
      "  copying lib\\cartopy\\tests\\lakes_shapefile\\ne_110m_lakes.dbf -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\lakes_shapefile\n",
      "  copying lib\\cartopy\\tests\\lakes_shapefile\\ne_110m_lakes.shp -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\lakes_shapefile\n",
      "  copying lib\\cartopy\\tests\\lakes_shapefile\\ne_110m_lakes.shx -> build\\lib.win-amd64-cpython-38\\cartopy\\tests\\lakes_shapefile\n",
      "  copying lib\\cartopy\\io\\srtm.npz -> build\\lib.win-amd64-cpython-38\\cartopy\\io\n",
      "  running build_ext\n",
      "  building 'cartopy.trace' extension\n",
      "  <string>:90: UserWarning: Unable to determine GEOS version. Ensure you have 3.7.2 or later installed, or installation may fail.\n",
      "  error: Microsoft Visual C++ 14.0 or greater is required. Get it with \"Microsoft C++ Build Tools\": https://visualstudio.microsoft.com/visual-cpp-build-tools/\n",
      "  ----------------------------------------\n",
      "  ERROR: Failed building wheel for cartopy\n",
      "ERROR: Could not build wheels for cartopy which use PEP 517 and cannot be installed directly\n"
     ]
    },
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'geoplot'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-76-ca25c145ad34>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mtqdm\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mtqdm_notebook\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mfolium\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplugins\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mMarkerCluster\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 11\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mgeoplot\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mgplt\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     12\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mgeopandas\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mgpd\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mgeoplot\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcrs\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mgcrs\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'geoplot'"
     ]
    }
   ],
   "source": [
    "!pip install folium\n",
    "!pip install geoplot\n",
    "!pip install imageio\n",
    "import pandas as pd\n",
    "import numpy as np \n",
    "import matplotlib.pyplot as plt \n",
    "import folium\n",
    "import imageio\n",
    "from tqdm import tqdm_notebook\n",
    "from folium.plugins import MarkerCluster\n",
    "import geoplot as gplt\n",
    "import geopandas as gpd\n",
    "import geoplot.crs as gcrs\n",
    "import imageio\n",
    "import mapclassify as mc\n",
    "import statsmodels.api as sm\n",
    "from statsmodels.tsa.stattools import adfuller\n",
    "from statsmodels.tsa.arima_model import ARIMA\n",
    "import scipy\n",
    "from itertools import product\n",
    "import seaborn as sns\n",
    "from statsmodels.graphics.tsaplots import plot_pacf\n",
    "from statsmodels.graphics.tsaplots import plot_acf\n",
    "from statsmodels.tsa.arima_process import ArmaProcess\n",
    "from statsmodels.stats.diagnostic import acorr_ljungbox\n",
    "from statsmodels.tsa.statespace.sarimax import SARIMAX\n",
    "from statsmodels.tsa.stattools import adfuller\n",
    "from statsmodels.tsa.stattools import pacf\n",
    "from statsmodels.tsa.stattools import acf\n",
    "\n",
    "plt.style.use('ggplot')\n",
    "plt.rcParams['font.family'] = 'sans-serif' \n",
    "plt.rcParams['font.serif'] = 'Ubuntu' \n",
    "plt.rcParams['font.monospace'] = 'Ubuntu Mono' \n",
    "plt.rcParams['font.size'] = 14 \n",
    "plt.rcParams['axes.labelsize'] = 12 \n",
    "plt.rcParams['axes.labelweight'] = 'bold' \n",
    "plt.rcParams['axes.titlesize'] = 12 \n",
    "plt.rcParams['xtick.labelsize'] = 12 \n",
    "plt.rcParams['ytick.labelsize'] = 12 \n",
    "plt.rcParams['legend.fontsize'] = 12 \n",
    "plt.rcParams['figure.titlesize'] = 12 \n",
    "plt.rcParams['image.cmap'] = 'jet' \n",
    "plt.rcParams['image.interpolation'] = 'none' \n",
    "plt.rcParams['figure.figsize'] = (12, 10) \n",
    "plt.rcParams['axes.grid']=True\n",
    "plt.rcParams['lines.linewidth'] = 2 \n",
    "plt.rcParams['lines.markersize'] = 8\n",
    "colors = ['xkcd:pale orange', 'xkcd:sea blue', 'xkcd:pale red', 'xkcd:sage green', 'xkcd:terra cotta', 'xkcd:dull purple', 'xkcd:teal', 'xkcd: goldenrod', 'xkcd:cadet blue',\n",
    "'xkcd:scarlet']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "      <th>weather</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2012-01-01</td>\n",
       "      <td>0.0</td>\n",
       "      <td>12.8</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4.7</td>\n",
       "      <td>drizzle</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2012-01-02</td>\n",
       "      <td>10.9</td>\n",
       "      <td>10.6</td>\n",
       "      <td>2.8</td>\n",
       "      <td>4.5</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2012-01-03</td>\n",
       "      <td>0.8</td>\n",
       "      <td>11.7</td>\n",
       "      <td>7.2</td>\n",
       "      <td>2.3</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2012-01-04</td>\n",
       "      <td>20.3</td>\n",
       "      <td>12.2</td>\n",
       "      <td>5.6</td>\n",
       "      <td>4.7</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2012-01-05</td>\n",
       "      <td>1.3</td>\n",
       "      <td>8.9</td>\n",
       "      <td>2.8</td>\n",
       "      <td>6.1</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2012-01-06</td>\n",
       "      <td>2.5</td>\n",
       "      <td>4.4</td>\n",
       "      <td>2.2</td>\n",
       "      <td>2.2</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2012-01-07</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.2</td>\n",
       "      <td>2.8</td>\n",
       "      <td>2.3</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2012-01-08</td>\n",
       "      <td>0.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>2.8</td>\n",
       "      <td>2.0</td>\n",
       "      <td>sun</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2012-01-09</td>\n",
       "      <td>4.3</td>\n",
       "      <td>9.4</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.4</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2012-01-10</td>\n",
       "      <td>1.0</td>\n",
       "      <td>6.1</td>\n",
       "      <td>0.6</td>\n",
       "      <td>3.4</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         date  precipitation  temp_max  temp_min  wind  weather\n",
       "0  2012-01-01            0.0      12.8       5.0   4.7  drizzle\n",
       "1  2012-01-02           10.9      10.6       2.8   4.5     rain\n",
       "2  2012-01-03            0.8      11.7       7.2   2.3     rain\n",
       "3  2012-01-04           20.3      12.2       5.6   4.7     rain\n",
       "4  2012-01-05            1.3       8.9       2.8   6.1     rain\n",
       "5  2012-01-06            2.5       4.4       2.2   2.2     rain\n",
       "6  2012-01-07            0.0       7.2       2.8   2.3     rain\n",
       "7  2012-01-08            0.0      10.0       2.8   2.0      sun\n",
       "8  2012-01-09            4.3       9.4       5.0   3.4     rain\n",
       "9  2012-01-10            1.0       6.1       0.6   3.4     rain"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "date             0\n",
       "precipitation    0\n",
       "temp_max         0\n",
       "temp_min         0\n",
       "wind             0\n",
       "weather          0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "rain       641\n",
       "sun        640\n",
       "fog        101\n",
       "drizzle     53\n",
       "snow        26\n",
       "Name: weather, dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['weather'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.bar(list(df['weather'].value_counts().keys()),(list(df['weather'].value_counts())))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sb.histplot(df['wind'])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th>wind</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2012-01-01</th>\n",
       "      <th>4.7</th>\n",
       "      <td>0.0</td>\n",
       "      <td>12.8</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-02</th>\n",
       "      <th>4.5</th>\n",
       "      <td>10.9</td>\n",
       "      <td>10.6</td>\n",
       "      <td>2.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-03</th>\n",
       "      <th>2.3</th>\n",
       "      <td>0.8</td>\n",
       "      <td>11.7</td>\n",
       "      <td>7.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-04</th>\n",
       "      <th>4.7</th>\n",
       "      <td>20.3</td>\n",
       "      <td>12.2</td>\n",
       "      <td>5.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2012-01-05</th>\n",
       "      <th>6.1</th>\n",
       "      <td>1.3</td>\n",
       "      <td>8.9</td>\n",
       "      <td>2.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-27</th>\n",
       "      <th>2.9</th>\n",
       "      <td>8.6</td>\n",
       "      <td>4.4</td>\n",
       "      <td>1.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-28</th>\n",
       "      <th>1.3</th>\n",
       "      <td>1.5</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-29</th>\n",
       "      <th>2.6</th>\n",
       "      <td>0.0</td>\n",
       "      <td>7.2</td>\n",
       "      <td>0.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-30</th>\n",
       "      <th>3.4</th>\n",
       "      <td>0.0</td>\n",
       "      <td>5.6</td>\n",
       "      <td>-1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2015-12-31</th>\n",
       "      <th>3.5</th>\n",
       "      <td>0.0</td>\n",
       "      <td>5.6</td>\n",
       "      <td>-2.1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1461 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                 precipitation  temp_max  temp_min\n",
       "date       wind                                   \n",
       "2012-01-01 4.7             0.0      12.8       5.0\n",
       "2012-01-02 4.5            10.9      10.6       2.8\n",
       "2012-01-03 2.3             0.8      11.7       7.2\n",
       "2012-01-04 4.7            20.3      12.2       5.6\n",
       "2012-01-05 6.1             1.3       8.9       2.8\n",
       "...                        ...       ...       ...\n",
       "2015-12-27 2.9             8.6       4.4       1.7\n",
       "2015-12-28 1.3             1.5       5.0       1.7\n",
       "2015-12-29 2.6             0.0       7.2       0.6\n",
       "2015-12-30 3.4             0.0       5.6      -1.0\n",
       "2015-12-31 3.5             0.0       5.6      -2.1\n",
       "\n",
       "[1461 rows x 3 columns]"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby(['date','wind'],sort=True).sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "      <th>weather</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>351</th>\n",
       "      <td>2012-12-17</td>\n",
       "      <td>2.0</td>\n",
       "      <td>8.3</td>\n",
       "      <td>1.7</td>\n",
       "      <td>9.5</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>700</th>\n",
       "      <td>2013-12-01</td>\n",
       "      <td>3.0</td>\n",
       "      <td>13.3</td>\n",
       "      <td>7.8</td>\n",
       "      <td>8.8</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>741</th>\n",
       "      <td>2014-01-11</td>\n",
       "      <td>21.3</td>\n",
       "      <td>14.4</td>\n",
       "      <td>7.2</td>\n",
       "      <td>8.8</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>2012-01-21</td>\n",
       "      <td>3.0</td>\n",
       "      <td>8.3</td>\n",
       "      <td>3.3</td>\n",
       "      <td>8.2</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>2012-02-18</td>\n",
       "      <td>6.4</td>\n",
       "      <td>6.7</td>\n",
       "      <td>3.9</td>\n",
       "      <td>8.1</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>418</th>\n",
       "      <td>2013-02-22</td>\n",
       "      <td>9.4</td>\n",
       "      <td>7.8</td>\n",
       "      <td>3.9</td>\n",
       "      <td>8.1</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>742</th>\n",
       "      <td>2014-01-12</td>\n",
       "      <td>1.5</td>\n",
       "      <td>11.1</td>\n",
       "      <td>5.6</td>\n",
       "      <td>8.1</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>120</th>\n",
       "      <td>2012-04-30</td>\n",
       "      <td>4.3</td>\n",
       "      <td>12.8</td>\n",
       "      <td>7.2</td>\n",
       "      <td>8.0</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1416</th>\n",
       "      <td>2015-11-17</td>\n",
       "      <td>29.5</td>\n",
       "      <td>13.3</td>\n",
       "      <td>6.7</td>\n",
       "      <td>8.0</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>671</th>\n",
       "      <td>2013-11-02</td>\n",
       "      <td>12.7</td>\n",
       "      <td>14.4</td>\n",
       "      <td>8.3</td>\n",
       "      <td>7.9</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            date  precipitation  temp_max  temp_min  wind weather\n",
       "351   2012-12-17            2.0       8.3       1.7   9.5    rain\n",
       "700   2013-12-01            3.0      13.3       7.8   8.8    rain\n",
       "741   2014-01-11           21.3      14.4       7.2   8.8    rain\n",
       "20    2012-01-21            3.0       8.3       3.3   8.2    rain\n",
       "48    2012-02-18            6.4       6.7       3.9   8.1    rain\n",
       "418   2013-02-22            9.4       7.8       3.9   8.1    rain\n",
       "742   2014-01-12            1.5      11.1       5.6   8.1    rain\n",
       "120   2012-04-30            4.3      12.8       7.2   8.0    rain\n",
       "1416  2015-11-17           29.5      13.3       6.7   8.0    rain\n",
       "671   2013-11-02           12.7      14.4       8.3   7.9    rain"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.nlargest(10,'wind')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "      <th>weather</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1169</th>\n",
       "      <td>2015-03-15</td>\n",
       "      <td>55.9</td>\n",
       "      <td>10.6</td>\n",
       "      <td>6.1</td>\n",
       "      <td>4.2</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>323</th>\n",
       "      <td>2012-11-19</td>\n",
       "      <td>54.1</td>\n",
       "      <td>13.3</td>\n",
       "      <td>8.3</td>\n",
       "      <td>6.0</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1437</th>\n",
       "      <td>2015-12-08</td>\n",
       "      <td>54.1</td>\n",
       "      <td>15.6</td>\n",
       "      <td>10.0</td>\n",
       "      <td>6.2</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1413</th>\n",
       "      <td>2015-11-14</td>\n",
       "      <td>47.2</td>\n",
       "      <td>9.4</td>\n",
       "      <td>6.1</td>\n",
       "      <td>4.5</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>794</th>\n",
       "      <td>2014-03-05</td>\n",
       "      <td>46.7</td>\n",
       "      <td>15.6</td>\n",
       "      <td>10.6</td>\n",
       "      <td>3.9</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            date  precipitation  temp_max  temp_min  wind weather\n",
       "1169  2015-03-15           55.9      10.6       6.1   4.2    rain\n",
       "323   2012-11-19           54.1      13.3       8.3   6.0    rain\n",
       "1437  2015-12-08           54.1      15.6      10.0   6.2    rain\n",
       "1413  2015-11-14           47.2       9.4       6.1   4.5    rain\n",
       "794   2014-03-05           46.7      15.6      10.6   3.9    rain"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "df.nlargest(5,'precipitation')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter precipitation 55.9\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "__call__() takes from 1 to 2 positional arguments but 3 were given",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-77-00b1e688df4c>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m     \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0miloc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'precipitation'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m==\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'wind'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mp\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0mpresp\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-77-00b1e688df4c>\u001b[0m in \u001b[0;36mpresp\u001b[1;34m(n)\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfloat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Enter precipitation\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mpresp\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0miloc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'precipitation'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m==\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'wind'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mp\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mpresp\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: __call__() takes from 1 to 2 positional arguments but 3 were given"
     ]
    }
   ],
   "source": [
    "n = float(input(\"Enter precipitation\"))\n",
    "def presp(n):\n",
    "    df.iloc(['precipitation']==n,['wind'])\n",
    "    return p\n",
    "presp(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "55.9"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['precipitation'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>precipitation</th>\n",
       "      <th>temp_max</th>\n",
       "      <th>temp_min</th>\n",
       "      <th>wind</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1461.000000</td>\n",
       "      <td>1461.000000</td>\n",
       "      <td>1461.000000</td>\n",
       "      <td>1461.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>3.029432</td>\n",
       "      <td>16.439083</td>\n",
       "      <td>8.234771</td>\n",
       "      <td>3.241136</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>6.680194</td>\n",
       "      <td>7.349758</td>\n",
       "      <td>5.023004</td>\n",
       "      <td>1.437825</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>-1.600000</td>\n",
       "      <td>-7.100000</td>\n",
       "      <td>0.400000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>10.600000</td>\n",
       "      <td>4.400000</td>\n",
       "      <td>2.200000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>15.600000</td>\n",
       "      <td>8.300000</td>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2.800000</td>\n",
       "      <td>22.200000</td>\n",
       "      <td>12.200000</td>\n",
       "      <td>4.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>55.900000</td>\n",
       "      <td>35.600000</td>\n",
       "      <td>18.300000</td>\n",
       "      <td>9.500000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       precipitation     temp_max     temp_min         wind\n",
       "count    1461.000000  1461.000000  1461.000000  1461.000000\n",
       "mean        3.029432    16.439083     8.234771     3.241136\n",
       "std         6.680194     7.349758     5.023004     1.437825\n",
       "min         0.000000    -1.600000    -7.100000     0.400000\n",
       "25%         0.000000    10.600000     4.400000     2.200000\n",
       "50%         0.000000    15.600000     8.300000     3.000000\n",
       "75%         2.800000    22.200000    12.200000     4.000000\n",
       "max        55.900000    35.600000    18.300000     9.500000"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "x = df.drop(columns = ['date','weather'],axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = df['weather']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      precipitation  temp_max  temp_min  wind\n",
      "0               0.0      12.8       5.0   4.7\n",
      "1              10.9      10.6       2.8   4.5\n",
      "2               0.8      11.7       7.2   2.3\n",
      "3              20.3      12.2       5.6   4.7\n",
      "4               1.3       8.9       2.8   6.1\n",
      "...             ...       ...       ...   ...\n",
      "1456            8.6       4.4       1.7   2.9\n",
      "1457            1.5       5.0       1.7   1.3\n",
      "1458            0.0       7.2       0.6   2.6\n",
      "1459            0.0       5.6      -1.0   3.4\n",
      "1460            0.0       5.6      -2.1   3.5\n",
      "\n",
      "[1461 rows x 4 columns]\n"
     ]
    }
   ],
   "source": [
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = DecisionTreeClassifier()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier()"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train_prediction = model.predict(x_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy score of training data :  0.9965753424657534\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score\n",
    "training_data_accuracy = accuracy_score(y_train, X_train_prediction)\n",
    "print('Accuracy score of training data : ', training_data_accuracy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy score of training data :  0.7713310580204779\n"
     ]
    }
   ],
   "source": [
    "X_test_prediction = model.predict(x_test)\n",
    "testing_data_accuracy = accuracy_score(y_test, X_test_prediction)\n",
    "print('Accuracy score of training data : ', testing_data_accuracy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Classification metrics can't handle a mix of continuous-multioutput and multiclass targets",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-70-267b707b07b4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmetrics\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mconfusion_matrix\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mcm_LR\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mconfusion_matrix\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx_train\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mX_train_prediction\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mcm_LR\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py\u001b[0m in \u001b[0;36minner_f\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m     70\u001b[0m                           FutureWarning)\n\u001b[0;32m     71\u001b[0m         \u001b[0mkwargs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m{\u001b[0m\u001b[0mk\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0marg\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mk\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0marg\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mzip\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msig\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 72\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     73\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0minner_f\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     74\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\metrics\\_classification.py\u001b[0m in \u001b[0;36mconfusion_matrix\u001b[1;34m(y_true, y_pred, labels, sample_weight, normalize)\u001b[0m\n\u001b[0;32m    274\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    275\u001b[0m     \"\"\"\n\u001b[1;32m--> 276\u001b[1;33m     \u001b[0my_type\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my_true\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my_pred\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_check_targets\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my_true\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0my_pred\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    277\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0my_type\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32min\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;34m\"binary\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"multiclass\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    278\u001b[0m         \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"%s is not supported\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0my_type\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\metrics\\_classification.py\u001b[0m in \u001b[0;36m_check_targets\u001b[1;34m(y_true, y_pred)\u001b[0m\n\u001b[0;32m     88\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     89\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my_type\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m>\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 90\u001b[1;33m         raise ValueError(\"Classification metrics can't handle a mix of {0} \"\n\u001b[0m\u001b[0;32m     91\u001b[0m                          \"and {1} targets\".format(type_true, type_pred))\n\u001b[0;32m     92\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: Classification metrics can't handle a mix of continuous-multioutput and multiclass targets"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "c_matrix=confusion_matrix(x_train, X_train_prediction)\n",
    "cm_LR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Target is multiclass but average='binary'. Please choose another average setting, one of [None, 'micro', 'macro', 'weighted'].",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-73-412743b32b40>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmetrics\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mprecision_score\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrecall_score\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mprecision_score\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my_train\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mX_train_prediction\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mrecall_score\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx_train\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mX_train_prediction\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py\u001b[0m in \u001b[0;36minner_f\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m     70\u001b[0m                           FutureWarning)\n\u001b[0;32m     71\u001b[0m         \u001b[0mkwargs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m{\u001b[0m\u001b[0mk\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0marg\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mk\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0marg\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mzip\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msig\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 72\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     73\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0minner_f\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     74\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\metrics\\_classification.py\u001b[0m in \u001b[0;36mprecision_score\u001b[1;34m(y_true, y_pred, labels, pos_label, average, sample_weight, zero_division)\u001b[0m\n\u001b[0;32m   1615\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1616\u001b[0m     \"\"\"\n\u001b[1;32m-> 1617\u001b[1;33m     p, _, _, _ = precision_recall_fscore_support(y_true, y_pred,\n\u001b[0m\u001b[0;32m   1618\u001b[0m                                                  \u001b[0mlabels\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mlabels\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1619\u001b[0m                                                  \u001b[0mpos_label\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mpos_label\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\utils\\validation.py\u001b[0m in \u001b[0;36minner_f\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m     70\u001b[0m                           FutureWarning)\n\u001b[0;32m     71\u001b[0m         \u001b[0mkwargs\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m{\u001b[0m\u001b[0mk\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0marg\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0mk\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0marg\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mzip\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msig\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0margs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 72\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mf\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     73\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0minner_f\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     74\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\metrics\\_classification.py\u001b[0m in \u001b[0;36mprecision_recall_fscore_support\u001b[1;34m(y_true, y_pred, beta, labels, pos_label, average, warn_for, sample_weight, zero_division)\u001b[0m\n\u001b[0;32m   1431\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mbeta\u001b[0m \u001b[1;33m<\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1432\u001b[0m         \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"beta should be >=0 in the F-beta score\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1433\u001b[1;33m     labels = _check_set_wise_labels(y_true, y_pred, average, labels,\n\u001b[0m\u001b[0;32m   1434\u001b[0m                                     pos_label)\n\u001b[0;32m   1435\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\sklearn\\metrics\\_classification.py\u001b[0m in \u001b[0;36m_check_set_wise_labels\u001b[1;34m(y_true, y_pred, average, labels, pos_label)\u001b[0m\n\u001b[0;32m   1261\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0my_type\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'multiclass'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1262\u001b[0m                 \u001b[0maverage_options\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mremove\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'samples'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1263\u001b[1;33m             raise ValueError(\"Target is %s but average='binary'. Please \"\n\u001b[0m\u001b[0;32m   1264\u001b[0m                              \u001b[1;34m\"choose another average setting, one of %r.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1265\u001b[0m                              % (y_type, average_options))\n",
      "\u001b[1;31mValueError\u001b[0m: Target is multiclass but average='binary'. Please choose another average setting, one of [None, 'micro', 'macro', 'weighted']."
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import precision_score, recall_score\n",
    "precision_score(y_train, X_train_prediction)\n",
    "recall_score(x_, X_train_prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "# checking algorithm\n",
    "\n",
    "from sklearn import tree\n",
    "#plt.figure(figsize=(30,10), facecolor ='k')\n",
    "\n",
    "#a = tree.plot_tree(model,feature_names = 'weather',class_names = ['precipitation','temp_max','temp_min','wind','class_names'],rounded = True,filled = True,fontsize=14)\n",
    "\n",
    "#plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "train_data_predict=model.predict(x_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['sun' 'sun' 'sun' ... 'sun' 'sun' 'rain']\n"
     ]
    }
   ],
   "source": [
    "print(train_data_predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import metrics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'labels' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-29-486b13ee75d6>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     15\u001b[0m \u001b[0max\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mset_xlabel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Predicted label\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfontsize\u001b[0m \u001b[1;33m=\u001b[0m\u001b[1;36m15\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     16\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 17\u001b[1;33m \u001b[0max\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mset_xticklabels\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m''\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0mlabels\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     18\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     19\u001b[0m \u001b[0max\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mset_ylabel\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"True Label\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfontsize\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m15\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'labels' is not defined"
     ]
    },
    {
     "data": {
      "image/png": "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YNiwYWjXrh1at26NHj16ICIiAn379pX8DilrvKysDP/88w/UajX27NmDp59+WrDtsmXLYLVanZ+joqIkv5/v+y5cuOCcyBiGQcuWLTFjxgyPtg6Xkkajkd1/ZGQkNmzYgCNHjmDv3r347bff8PXXX+Ppp5/GlClTZPXB9yzyyUCCWJa74cswDLRaLW8oqeN5k3O/quA7qnzwPKBpGn379sW6detcrB4HPv/8c+zfvx8JCQlISkqCRqPBgQMHXNocOHAAarVa0uIUg0ajcfF9l5aWIj8/3/n5m2++wdq1a9GuXTuMGTMG69evx6OPPooNGzZ49OXYiDt69KjL8T/++AP169f3WUZ39OrVCz/99BM2bdqEli1bOpfmXKxYsQIpKSlYsmQJhg4dio4dOyInJwdAhZLxNqzSgYyMDBgMBqxcuRK7d+8WjZFPSEhAYmKi859jteINvvzyS1AUhV69egEAGjRogAsXLiA2NtbZb7Vq1fD+++87n5GkpCSP3+HTTz/F448/7tH/jz/+iI8++ggtWrTAq6++ii+++AIvvfQS1q9f79E2OTkZADyexT/++AMRERE+TWD+IDk5GWazGSUlJS73+ZtvvnE+o3LuVxV8R5WCF8DLL7+MevXqYcCAAVi/fj0uXbqEkydP4v3338f8+fPx+uuvIykpCcHBwXj66afx0UcfOdt9++23WLBgAfr27YuIiAifZUhNTcU333yDv//+G2fOnMGECRNcQhANBgPee+89bNq0CVevXsWBAwdw6NAhXl95+/bt0aRJE0yYMAF79+7FP//8g/nz52PXrl2yrX056NKlC1iWxYIFC3jdMwBQvXp1nDt3Dvv378fVq1exdetWpzXqWKE4wjuPHj2KsrIyWd+9bds2rF+/HhkZGWjTpg1efPFFvPvuuzh//rzf42IYBrm5ucjNzUV2djZOnTqF2bNnY/78+Xjttdec+x7PPPMMjEYjXn/9dRw7dgznzp3DuHHjsHfvXjRs2BAA8NJLL+HHH3/E8uXLcenSJezatQsfffQRunbt6vG9NE1jwYIF+Oyzz3D58mX8/fff2L17N+9vnJSUhK5du2LmzJn48ccfcenSJaxatQpfffUVnn/++dser+545saOHYtff/0Vly9fxuLFi/Hxxx87DR8596sKvqPKRSMAvV6Pzz77DJ9++ik++eQTZGRkQK1W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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 720x504 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "confusion_matrix = metrics.confusion_matrix(y_train,train_data_predict)\n",
    "\n",
    "matrix_df = pd.DataFrame(confusion_matrix)\n",
    "\n",
    "ax = plt.axes()\n",
    "\n",
    "sb.set(font_scale=1.3)\n",
    "\n",
    "plt.figure(figsize=(10,7))\n",
    "\n",
    "sb.heatmap(x, annot=True, fmt=\"g\", ax=ax, cmap=\"magma\")\n",
    "\n",
    "ax.set_title('Confusion Matrix - Decision Tree')\n",
    "\n",
    "ax.set_xlabel(\"Predicted label\", fontsize =15)\n",
    "\n",
    "ax.set_xticklabels(['']+)\n",
    "\n",
    "ax.set_ylabel(\"True Label\", fontsize=15)\n",
    "\n",
    "ax.set_yticklabels(list(labels), rotation = 0)\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

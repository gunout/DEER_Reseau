import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import os

class ReunionRoutesAnalysis:
    def __init__(self):
        # Créer un dossier pour les résultats s'il n'existe pas
        if not os.path.exists('results'):
            os.makedirs('results')
        
        # Données historiques des routes à La Réunion (longueur en km)
        self.routes_data = {
            '2002': {
                'routes_departementales': 1200, 'routes_regionales': 450, 'routes_communales': 2800,
                'ponts_et_viaducs': 45, 'tunnels': 12, 'voies_express': 85,
                'routes_nationales': 180, 'chemins_ruraux': 3500, 'sentiers_pietons': 1200,
                'pistes_cyclables': 150, 'voies_bus': 75, 'ronds_points': 280,
                'carrefours_giratoires': 95, 'ouvrages_art': 320, 'barrieres_securite': 4200
            },
            '2003': {
                'routes_departementales': 1215, 'routes_regionales': 455, 'routes_communales': 2820,
                'ponts_et_viaducs': 46, 'tunnels': 13, 'voies_express': 87,
                'routes_nationales': 182, 'chemins_ruraux': 3520, 'sentiers_pietons': 1220,
                'pistes_cyclables': 160, 'voies_bus': 78, 'ronds_points': 290,
                'carrefours_giratoires': 98, 'ouvrages_art': 330, 'barrieres_securite': 4250
            },
            '2004': {
                'routes_departementales': 1230, 'routes_regionales': 460, 'routes_communales': 2840,
                'ponts_et_viaducs': 47, 'tunnels': 14, 'voies_express': 89,
                'routes_nationales': 184, 'chemins_ruraux': 3540, 'sentiers_pietons': 1240,
                'pistes_cyclables': 170, 'voies_bus': 81, 'ronds_points': 300,
                'carrefours_giratoires': 101, 'ouvrages_art': 340, 'barrieres_securite': 4300
            },
            '2005': {
                'routes_departementales': 1245, 'routes_regionales': 465, 'routes_communales': 2860,
                'ponts_et_viaducs': 48, 'tunnels': 15, 'voies_express': 91,
                'routes_nationales': 186, 'chemins_ruraux': 3560, 'sentiers_pietons': 1260,
                'pistes_cyclables': 180, 'voies_bus': 84, 'ronds_points': 310,
                'carrefours_giratoires': 104, 'ouvrages_art': 350, 'barrieres_securite': 4350
            },
            '2006': {
                'routes_departementales': 1260, 'routes_regionales': 470, 'routes_communales': 2880,
                'ponts_et_viaducs': 49, 'tunnels': 16, 'voies_express': 93,
                'routes_nationales': 188, 'chemins_ruraux': 3580, 'sentiers_pietons': 1280,
                'pistes_cyclables': 190, 'voies_bus': 87, 'ronds_points': 320,
                'carrefours_giratoires': 107, 'ouvrages_art': 360, 'barrieres_securite': 4400
            },
            '2007': {
                'routes_departementales': 1275, 'routes_regionales': 475, 'routes_communales': 2900,
                'ponts_et_viaducs': 50, 'tunnels': 17, 'voies_express': 95,
                'routes_nationales': 190, 'chemins_ruraux': 3600, 'sentiers_pietons': 1300,
                'pistes_cyclables': 200, 'voies_bus': 90, 'ronds_points': 330,
                'carrefours_giratoires': 110, 'ouvrages_art': 370, 'barrieres_securite': 4450
            },
            '2008': {
                'routes_departementales': 1290, 'routes_regionales': 480, 'routes_communales': 2920,
                'ponts_et_viaducs': 51, 'tunnels': 18, 'voies_express': 97,
                'routes_nationales': 192, 'chemins_ruraux': 3620, 'sentiers_pietons': 1320,
                'pistes_cyclables': 210, 'voies_bus': 93, 'ronds_points': 340,
                'carrefours_giratoires': 113, 'ouvrages_art': 380, 'barrieres_securite': 4500
            },
            '2009': {
                'routes_departementales': 1305, 'routes_regionales': 485, 'routes_communales': 2940,
                'ponts_et_viaducs': 52, 'tunnels': 19, 'voies_express': 99,
                'routes_nationales': 194, 'chemins_ruraux': 3640, 'sentiers_pietons': 1340,
                'pistes_cyclables': 220, 'voies_bus': 96, 'ronds_points': 350,
                'carrefours_giratoires': 116, 'ouvrages_art': 390, 'barrieres_securite': 4550
            },
            '2010': {
                'routes_departementales': 1320, 'routes_regionales': 490, 'routes_communales': 2960,
                'ponts_et_viaducs': 53, 'tunnels': 20, 'voies_express': 101,
                'routes_nationales': 196, 'chemins_ruraux': 3660, 'sentiers_pietons': 1360,
                'pistes_cyclables': 230, 'voies_bus': 99, 'ronds_points': 360,
                'carrefours_giratoires': 119, 'ouvrages_art': 400, 'barrieres_securite': 4600
            },
            '2011': {
                'routes_departementales': 1340, 'routes_regionales': 495, 'routes_communales': 2980,
                'ponts_et_viaducs': 54, 'tunnels': 21, 'voies_express': 103,
                'routes_nationales': 198, 'chemins_ruraux': 3680, 'sentiers_pietons': 1380,
                'pistes_cyclables': 240, 'voies_bus': 102, 'ronds_points': 370,
                'carrefours_giratoires': 122, 'ouvrages_art': 410, 'barrieres_securite': 4650
            },
            '2012': {
                'routes_departementales': 1360, 'routes_regionales': 500, 'routes_communales': 3000,
                'ponts_et_viaducs': 55, 'tunnels': 22, 'voies_express': 105,
                'routes_nationales': 200, 'chemins_ruraux': 3700, 'sentiers_pietons': 1400,
                'pistes_cyclables': 250, 'voies_bus': 105, 'ronds_points': 380,
                'carrefours_giratoires': 125, 'ouvrages_art': 420, 'barrieres_securite': 4700
            },
            '2013': {
                'routes_departementales': 1380, 'routes_regionales': 505, 'routes_communales': 3020,
                'ponts_et_viaducs': 56, 'tunnels': 23, 'voies_express': 107,
                'routes_nationales': 202, 'chemins_ruraux': 3720, 'sentiers_pietons': 1420,
                'pistes_cyclables': 260, 'voies_bus': 108, 'ronds_points': 390,
                'carrefours_giratoires': 128, 'ouvrages_art': 430, 'barrieres_securite': 4750
            },
            '2014': {
                'routes_departementales': 1400, 'routes_regionales': 510, 'routes_communales': 3040,
                'ponts_et_viaducs': 57, 'tunnels': 24, 'voies_express': 109,
                'routes_nationales': 204, 'chemins_ruraux': 3740, 'sentiers_pietons': 1440,
                'pistes_cyclables': 270, 'voies_bus': 111, 'ronds_points': 400,
                'carrefours_giratoires': 131, 'ouvrages_art': 440, 'barrieres_securite': 4800
            },
            '2015': {
                'routes_departementales': 1420, 'routes_regionales': 515, 'routes_communales': 3060,
                'ponts_et_viaducs': 58, 'tunnels': 25, 'voies_express': 111,
                'routes_nationales': 206, 'chemins_ruraux': 3760, 'sentiers_pietons': 1460,
                'pistes_cyclables': 280, 'voies_bus': 114, 'ronds_points': 410,
                'carrefours_giratoires': 134, 'ouvrages_art': 450, 'barrieres_securite': 4850
            },
            '2016': {
                'routes_departementales': 1440, 'routes_regionales': 520, 'routes_communales': 3080,
                'ponts_et_viaducs': 59, 'tunnels': 26, 'voies_express': 113,
                'routes_nationales': 208, 'chemins_ruraux': 3780, 'sentiers_pietons': 1480,
                'pistes_cyclables': 290, 'voies_bus': 117, 'ronds_points': 420,
                'carrefours_giratoires': 137, 'ouvrages_art': 460, 'barrieres_securite': 4900
            },
            '2017': {
                'routes_departementales': 1460, 'routes_regionales': 525, 'routes_communales': 3100,
                'ponts_et_viaducs': 60, 'tunnels': 27, 'voies_express': 115,
                'routes_nationales': 210, 'chemins_ruraux': 3800, 'sentiers_pietons': 1500,
                'pistes_cyclables': 300, 'voies_bus': 120, 'ronds_points': 430,
                'carrefours_giratoires': 140, 'ouvrages_art': 470, 'barrieres_securite': 4950
            },
            '2018': {
                'routes_departementales': 1480, 'routes_regionales': 530, 'routes_communales': 3120,
                'ponts_et_viaducs': 61, 'tunnels': 28, 'voies_express': 117,
                'routes_nationales': 212, 'chemins_ruraux': 3820, 'sentiers_pietons': 1520,
                'pistes_cyclables': 310, 'voies_bus': 123, 'ronds_points': 440,
                'carrefours_giratoires': 143, 'ouvrages_art': 480, 'barrieres_securite': 5000
            },
            '2019': {
                'routes_departementales': 1500, 'routes_regionales': 535, 'routes_communales': 3140,
                'ponts_et_viaducs': 62, 'tunnels': 29, 'voies_express': 119,
                'routes_nationales': 214, 'chemins_ruraux': 3840, 'sentiers_pietons': 1540,
                'pistes_cyclables': 320, 'voies_bus': 126, 'ronds_points': 450,
                'carrefours_giratoires': 146, 'ouvrages_art': 490, 'barrieres_securite': 5050
            },
            '2020': {
                'routes_departementales': 1525, 'routes_regionales': 540, 'routes_communales': 3160,
                'ponts_et_viaducs': 63, 'tunnels': 30, 'voies_express': 121,
                'routes_nationales': 216, 'chemins_ruraux': 3860, 'sentiers_pietons': 1560,
                'pistes_cyclables': 330, 'voies_bus': 129, 'ronds_points': 460,
                'carrefours_giratoires': 149, 'ouvrages_art': 500, 'barrieres_securite': 5100
            },
            '2021': {
                'routes_departementales': 1550, 'routes_regionales': 545, 'routes_communales': 3180,
                'ponts_et_viaducs': 64, 'tunnels': 31, 'voies_express': 123,
                'routes_nationales': 218, 'chemins_ruraux': 3880, 'sentiers_pietons': 1580,
                'pistes_cyclables': 340, 'voies_bus': 132, 'ronds_points': 470,
                'carrefours_giratoires': 152, 'ouvrages_art': 510, 'barrieres_securite': 5150
            },
            '2022': {
                'routes_departementales': 1575, 'routes_regionales': 550, 'routes_communales': 3200,
                'ponts_et_viaducs': 65, 'tunnels': 32, 'voies_express': 125,
                'routes_nationales': 220, 'chemins_ruraux': 3900, 'sentiers_pietons': 1600,
                'pistes_cyclables': 350, 'voies_bus': 135, 'ronds_points': 480,
                'carrefours_giratoires': 155, 'ouvrages_art': 520, 'barrieres_securite': 5200
            },
            '2023': {
                'routes_departementales': 1600, 'routes_regionales': 555, 'routes_communales': 3220,
                'ponts_et_viaducs': 66, 'tunnels': 33, 'voies_express': 127,
                'routes_nationales': 222, 'chemins_ruraux': 3920, 'sentiers_pietons': 1620,
                'pistes_cyclables': 360, 'voies_bus': 138, 'ronds_points': 490,
                'carrefours_giratoires': 158, 'ouvrages_art': 530, 'barrieres_securite': 5250
            },
            '2024': {
                'routes_departementales': 1625, 'routes_regionales': 560, 'routes_communales': 3240,
                'ponts_et_viaducs': 67, 'tunnels': 34, 'voies_express': 129,
                'routes_nationales': 224, 'chemins_ruraux': 3940, 'sentiers_pietons': 1640,
                'pistes_cyclables': 370, 'voies_bus': 141, 'ronds_points': 500,
                'carrefours_giratoires': 161, 'ouvrages_art': 540, 'barrieres_securite': 5300
            },
            '2025': {
                'routes_departementales': 1650, 'routes_regionales': 565, 'routes_communales': 3260,
                'ponts_et_viaducs': 68, 'tunnels': 35, 'voies_express': 131,
                'routes_nationales': 226, 'chemins_ruraux': 3960, 'sentiers_pietons': 1660,
                'pistes_cyclables': 380, 'voies_bus': 144, 'ronds_points': 510,
                'carrefours_giratoires': 164, 'ouvrages_art': 550, 'barrieres_securite': 5350
            }
        }
        
        # Budgets d'investissement routier (en millions d'euros)
        self.investment_budgets = {
            '2002': 85, '2003': 88, '2004': 92, '2005': 95, '2006': 98,
            '2007': 102, '2008': 105, '2009': 108, '2010': 112, '2011': 115,
            '2012': 120, '2013': 125, '2014': 130, '2015': 135, '2016': 140,
            '2017': 145, '2018': 150, '2019': 155, '2020': 160, '2021': 165,
            '2022': 170, '2023': 175, '2024': 180, '2025': 185
        }
        
        # Population de La Réunion (en milliers)
        self.population_data = {
            '2002': 750, '2003': 765, '2004': 780, '2005': 795, '2006': 810,
            '2007': 825, '2008': 840, '2009': 855, '2010': 870, '2011': 885,
            '2012': 900, '2013': 915, '2014': 930, '2015': 945, '2016': 960,
            '2017': 975, '2018': 990, '2019': 1005, '2020': 1020, '2021': 1035,
            '2022': 1050, '2023': 1065, '2024': 1080, '2025': 1095
        }
        
        # Création du DataFrame
        self.df = pd.DataFrame.from_dict(self.routes_data, orient='index')
        self.df.index = pd.to_datetime(self.df.index, format='%Y')
        
        # Properly add investment_budget and population columns
        # Convert to series with the same index
        investment_series = pd.Series(self.investment_budgets, name='investment_budget')
        investment_series.index = pd.to_datetime(investment_series.index, format='%Y')
        
        population_series = pd.Series(self.population_data, name='population')
        population_series.index = pd.to_datetime(population_series.index, format='%Y')
        
        # Merge with the main dataframe
        self.df = self.df.merge(investment_series, left_index=True, right_index=True)
        self.df = self.df.merge(population_series, left_index=True, right_index=True)
        
        # Exporter les données en CSV
        self.export_data_to_csv()
    
    def export_data_to_csv(self):
        """Exporter toutes les données en CSV"""
        # Données principales
        self.df.to_csv('results/donnees_routieres_completes.csv')
        
        # Données de croissance
        croissance_data = {}
        for col in ['routes_departementales', 'routes_regionales', 'routes_communales', 
                   'routes_nationales', 'pistes_cyclables']:
            start = self.df[col].iloc[0]
            end = self.df[col].iloc[-1]
            croissance_data[col] = [start, end, ((end - start) / start) * 100]
        
        croissance_df = pd.DataFrame.from_dict(croissance_data, orient='index', 
                                             columns=['2002', '2025', 'Croissance (%)'])
        croissance_df.to_csv('results/croissance_routiere.csv')
        
        # Statistiques descriptives
        stats_df = self.df[['routes_departementales', 'routes_regionales', 'routes_communales']].describe()
        stats_df.to_csv('results/statistiques_descriptives.csv')
        
        print("Données exportées en CSV dans le dossier 'results'")
    
    def plot_evolution_principale(self):
        """Évolution des routes principales et sauvegarde en PNG"""
        fig, ax = plt.subplots(2, 2, figsize=(15, 12))
        
        # Routes principales
        ax[0, 0].plot(self.df.index, self.df['routes_departementales'], 'b-', label='Départementales', linewidth=2)
        ax[0, 0].plot(self.df.index, self.df['routes_regionales'], 'r-', label='Régionales', linewidth=2)
        ax[0, 0].plot(self.df.index, self.df['routes_communales'], 'g-', label='Communales', linewidth=2)
        ax[0, 0].set_title('Évolution des Routes à La Réunion (2002-2025)', fontsize=14, fontweight='bold')
        ax[0, 0].set_xlabel('Année')
        ax[0, 0].set_ylabel('Longueur (km)')
        ax[0, 0].legend()
        ax[0, 0].grid(True, alpha=0.3)
        
        # Routes nationales et voies express
        ax[0, 1].plot(self.df.index, self.df['routes_nationales'], 'purple', label='Nationales', linewidth=2)
        ax[0, 1].plot(self.df.index, self.df['voies_express'], 'orange', label='Voies Express', linewidth=2)
        ax[0, 1].set_title('Routes Nationales et Voies Express', fontsize=14, fontweight='bold')
        ax[0, 1].set_xlabel('Année')
        ax[0, 1].set_ylabel('Longueur (km)')
        ax[0, 1].legend()
        ax[0, 1].grid(True, alpha=0.3)
        
        # Infrastructures de transport doux
        ax[1, 0].plot(self.df.index, self.df['pistes_cyclables'], 'cyan', label='Pistes Cyclables', linewidth=2)
        ax[1, 0].plot(self.df.index, self.df['sentiers_pietons'], 'brown', label='Sentiers Piétons', linewidth=2)
        ax[1, 0].plot(self.df.index, self.df['voies_bus'], 'magenta', label='Voies Bus', linewidth=2)
        ax[1, 0].set_title('Infrastructures de Transport Doux', fontsize=14, fontweight='bold')
        ax[1, 0].set_xlabel('Année')
        ax[1, 0].set_ylabel('Longueur (km)')
        ax[1, 0].legend()
        ax[1, 0].grid(True, alpha=0.3)
        
        # Ouvrages d'art
        ax[1, 1].plot(self.df.index, self.df['ponts_et_viaducs'], 'red', label='Ponts et Viaducs', linewidth=2)
        ax[1, 1].plot(self.df.index, self.df['tunnels'], 'black', label='Tunnels', linewidth=2)
        ax[1, 1].plot(self.df.index, self.df['ouvrages_art'], 'gray', label='Ouvrages d\'Art', linewidth=2)
        ax[1, 1].set_title('Ouvrages d\'Art et Infrastructures', fontsize=14, fontweight='bold')
        ax[1, 1].set_xlabel('Année')
        ax[1, 1].set_ylabel('Nombre')
        ax[1, 1].legend()
        ax[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('results/evolution_routes_principales.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("Graphique 'evolution_routes_principales.png' sauvegardé")
    
    def plot_croissance_relative(self):
        """Croissance relative des différents types de routes et sauvegarde en PNG"""
        fig, ax = plt.subplots(1, 2, figsize=(15, 6))
        
        # Calcul des pourcentages de croissance
        croissance = {}
        for col in ['routes_departementales', 'routes_regionales', 'routes_communales', 
                   'routes_nationales', 'pistes_cyclables']:
            start = self.df[col].iloc[0]
            end = self.df[col].iloc[-1]
            croissance[col] = ((end - start) / start) * 100
        
        # Diagramme en barres de la croissance
        categories = ['Départementales', 'Régionales', 'Communales', 'Nationales', 'Pistes Cyclables']
        valeurs = [croissance['routes_departementales'], croissance['routes_regionales'],
                  croissance['routes_communales'], croissance['routes_nationales'],
                  croissance['pistes_cyclables']]
        
        bars = ax[0].bar(categories, valeurs, color=['blue', 'red', 'green', 'purple', 'cyan'])
        ax[0].set_title('Croissance Relative des Routes (2002-2025)', fontsize=14, fontweight='bold')
        ax[0].set_ylabel('Croissance (%)')
        ax[0].tick_params(axis='x', rotation=45)
        
        # Ajouter les valeurs sur les barres
        for bar, valeur in zip(bars, valeurs):
            height = bar.get_height()
            ax[0].text(bar.get_x() + bar.get_width()/2., height + 0.5,
                    f'{valeur:.1f}%', ha='center', va='bottom')
        
        # Densité routière par habitant
        df_temp = self.df.copy()
        df_temp['densite_totale'] = (df_temp['routes_departementales'] + 
                                   df_temp['routes_regionales'] + 
                                   df_temp['routes_communales']) / df_temp['population']
        
        ax[1].plot(df_temp.index, df_temp['densite_totale'], 'b-', linewidth=2)
        ax[1].set_title('Densité Routière (km/1000 habitants)', fontsize=14, fontweight='bold')
        ax[1].set_xlabel('Année')
        ax[1].set_ylabel('km/1000 habitants')
        ax[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('results/croissance_relative_densite.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("Graphique 'croissance_relative_densite.png' sauvegardé")
    
    def plot_investissements(self):
        """Analyse des investissements et sauvegarde en PNG"""
        fig, ax = plt.subplots(1, 2, figsize=(15, 6))
        
        # Budget d'investissement
        ax[0].plot(self.df.index, self.df['investment_budget'], 'r-', linewidth=2)
        ax[0].set_title('Budget d\'Investissement Routier', fontsize=14, fontweight='bold')
        ax[0].set_xlabel('Année')
        ax[0].set_ylabel('Millions d\'euros')
        ax[0].grid(True, alpha=0.3)
        
        # Investissement par km de route
        df_temp = self.df.copy()
        df_temp['routes_totales'] = (df_temp['routes_departementales'] + 
                                   df_temp['routes_regionales'] + 
                                   df_temp['routes_communales'])
        df_temp['invest_par_km'] = df_temp['investment_budget'] * 1e6 / df_temp['routes_totales']
        
        ax[1].plot(df_temp.index, df_temp['invest_par_km'], 'g-', linewidth=2)
        ax[1].set_title('Investissement par km de Route', fontsize=14, fontweight='bold')
        ax[1].set_xlabel('Année')
        ax[1].set_ylabel('Euros/km')
        ax[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('results/analyse_investissements.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("Graphique 'analyse_investissements.png' sauvegardé")
    
    def statistiques_descriptives(self):
        """Affiche les statistiques descriptives"""
        print("=" * 60)
        print("STATISTIQUES DESCRIPTIVES - RÉSEAU ROUTIER DE LA RÉUNION")
        print("=" * 60)
        
        # Routes principales
        routes_principales = self.df[['routes_departementales', 'routes_regionales', 'routes_communales']]
        stats = routes_principales.describe()
        print("\nRoutes Principales (en km):")
        print(stats)
        
        # Croissance totale
        total_2002 = routes_principales.iloc[0].sum()
        total_2025 = routes_principales.iloc[-1].sum()
        croissance_totale = ((total_2025 - total_2002) / total_2002) * 100
        
        print(f"\nCroissance totale du réseau routier (2002-2025): {croissance_totale:.2f}%")
        print(f"Longueur totale en 2002: {total_2002} km")
        print(f"Longueur totale en 2025: {total_2025} km")
        print(f"Augmentation: {total_2025 - total_2002} km")
        
        # Investissements
        invest_total = self.df['investment_budget'].sum()
        print(f"\nInvestissement total (2002-2025): {invest_total:.2f} millions d'euros")
        
        # Densité routière moyenne
        total_routes = (self.df['routes_departementales'] + 
                       self.df['routes_regionales'] + 
                       self.df['routes_communales'])
        densite_moyenne = total_routes.mean() / self.df['population'].mean() * 1000
        print(f"Densité routière moyenne: {densite_moyenne:.2f} km/1000 habitants")
    
    def analyse_avancee(self):
        """Analyses avancées et prédictions"""
        from sklearn.linear_model import LinearRegression
        from sklearn.preprocessing import PolynomialFeatures
        from sklearn.pipeline import Pipeline
        
        print("\n" + "=" * 60)
        print("ANALYSE AVANCÉE ET PROJECTIONS")
        print("=" * 60)
        
        # Préparation des données
        X = np.array(range(len(self.df))).reshape(-1, 1)  # Années comme variable
        y_dep = self.df['routes_departementales'].values
        y_reg = self.df['routes_regionales'].values
        y_com = self.df['routes_communales'].values
        
        # Modèle polynomial pour les départementales
        model_dep = Pipeline([
            ('poly', PolynomialFeatures(degree=2)),
            ('linear', LinearRegression())
        ])
        model_dep.fit(X, y_dep)
        
        # Prédiction pour 2030
        future_years = np.array(range(len(self.df), len(self.df) + 6)).reshape(-1, 1)
        pred_dep = model_dep.predict(future_years)
        
        print(f"Projection des routes départementales en 2030: {pred_dep[-1]:.0f} km")
        print(f"Soit une croissance de {(pred_dep[-1] - y_dep[-1])/y_dep[-1]*100:.1f}% par rapport à 2025")
        
        # Taux de croissance annuel moyen
        taux_croissance_dep = (y_dep[-1] / y_dep[0]) ** (1/len(self.df)) - 1
        print(f"\nTaux de croissance annuel moyen des routes départementales: {taux_croissance_dep*100:.2f}%")
        
        # Analyse de corrélation
        correlation = self.df[['investment_budget', 'routes_departementales', 
                              'routes_regionales', 'routes_communales']].corr()
        print("\nMatrice de corrélation:")
        print(correlation)
        
        # Sauvegarder la matrice de corrélation
        correlation.to_csv('results/matrice_correlation.csv')
        print("Matrice de corrélation sauvegardée dans 'results/matrice_correlation.csv'")
    
    def run_complete_analysis(self):
        """Exécute l'analyse complète"""
        print("ANALYSE DU RÉSEAU ROUTIER DE LA RÉUNION")
        print("Évolution 2002-2025\n")
        
        self.plot_evolution_principale()
        self.plot_croissance_relative()
        self.plot_investissements()
        self.statistiques_descriptives()
        self.analyse_avancee()
        
        print("\n" + "=" * 60)
        print("ANALYSE TERMINÉE")
        print("Graphiques sauvegardés dans le dossier 'results'")
        print("Données exportées en format CSV")
        print("=" * 60)

# Exécution du programme
if __name__ == "__main__":
    analysis = ReunionRoutesAnalysis()
    analysis.run_complete_analysis()
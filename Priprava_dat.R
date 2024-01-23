
setwd("C:/Users/cerma/R/Diplomova_prace/")
rm(list = ls())
#Načtení knihoven
library(readxl)
library(tidyverse)
library(stringr)
library(ggplot2)

#Příprava čtvrtletního GDP
#Sezónně očištěné GDP, zdroj ČSU
GDP <- read_excel("C:/Users/cerma/R/Diplomova_prace/Data1.xlsx", 
                    sheet = "stálé(L)2015_mil", range = "A13:C128")
GDP <- GDP %>% mutate(Year=as.numeric(...1),
                          Quarter=...2,
                          GDP=as.numeric(...3))
GDP <- GDP %>% select(Year,Quarter,GDP)
GDP$GDP[GDP$GDP == "."] <- NA
GDP <- GDP %>% mutate(GDP_change = ((GDP - lag(GDP))/lag(GDP)) * 100)


# Index spotřebitelských cen
# Změna metodiky 2017/2018 
# Od ledna 2017 byla zavedena časová řada bazických indexů se základem průměr roku 2015 = 100
# Zdroj: Veřejná databáze ČSU https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt&pvo=CEN080&z=T&f=TABULKA&skupId=43&katalog=31779&pvo=CEN080&evo=v2300_!_CEN-SPO-BAZIC2005-M_1#w=
CPI_2017 <- read_excel("CEN080.xlsx", range = "B8:C283", 
                     col_names = c("Date","CPI"))
CPI_2017 <- CPI_2017 %>% mutate(Month=as.numeric(str_extract(Date,"[0-9]{2}")),
                      Year = as.numeric(str_extract(Date,"[0-9]{4}$"))
                      ) %>% mutate(Month = case_when(Month == 01 ~ "January",
                                                     Month == 02 ~ "February",
                                                     Month == 03 ~ "March",
                                                     Month == 04 ~ "April",
                                                     Month == 05 ~ "May",
                                                     Month == 06 ~ "June",
                                                     Month == 07 ~ "July",
                                                     Month == 08 ~ "August",
                                                     Month == 09 ~ "September",
                                                     Month == 10 ~ "October",
                                                     Month == 11 ~ "November",
                                                     Month == 12 ~ "December",)) %>%
  mutate(Month =factor(Month,levels = c("January","February", "March","April",
                                        "May","June","July","August","September",
                                        "October","November","December"))) %>%
  select(Year,Month,CPI)

CPI_2018 <- read_excel("CEN083A.xlsx", range = "B8:C79", 
                       col_names = c("Date","CPI"))

CPI_2018 <- CPI_2018 %>% mutate(Month=as.numeric(str_extract(Date,"[0-9]{2}")),
                      Year = as.numeric(str_extract(Date,"[0-9]{4}$"))
) %>% mutate(Month = case_when(Month == 01 ~ "January",
                               Month == 02 ~ "February",
                               Month == 03 ~ "March",
                               Month == 04 ~ "April",
                               Month == 05 ~ "May",
                               Month == 06 ~ "June",
                               Month == 07 ~ "July",
                               Month == 08 ~ "August",
                               Month == 09 ~ "September",
                               Month == 10 ~ "October",
                               Month == 11 ~ "November",
                               Month == 12 ~ "December",)) %>%
  mutate(Month =factor(Month,levels = c("January","February", "March","April",
                                        "May","June","July","August","September",
                                        "October","November","December"))) %>%
  select(Year,Month,CPI)

CPI <- rbind(CPI_2017,CPI_2018)

# Inflace z Eurostatu
Euro_CPI <- read_tsv("estat_prc_hicp_midx.tsv",col_names = c("freq,unit,coicop,geo"))
Euro_CPI <- Euro_CPI %>% separate(`freq,unit,coicop,geo`,
                                  c("freq","unit","coicop","geo","time_period"),sep = ",|\\\\"
                                  ) 
second_row <- Euro_CPI[1, ]
colnames(Euro_CPI) <- second_row

Euro_CPI <- Euro_CPI %>% filter(geo=="CZ"&coicop=="CP00") %>% 
  pivot_longer(cols = -c("freq","unit","coicop","geo","TIME_PERIOD"),
               names_to = "Date",
               values_to = "CPI") %>% mutate(Month=as.numeric(str_extract(Date,"[0-9]{2}$")),
                                             Year = as.numeric(str_extract(Date,"^[0-9]{4}"))
               ) %>% mutate(Month = case_when(Month == 01 ~ "January",
                                          Month == 02 ~ "February",
                                          Month == 03 ~ "March",
                                          Month == 04 ~ "April",
                                          Month == 05 ~ "May",
                                          Month == 06 ~ "June",
                                          Month == 07 ~ "July",
                                          Month == 08 ~ "August",
                                          Month == 09 ~ "September",
                                          Month == 10 ~ "October",
                                          Month == 11 ~ "November",
                                          Month == 12 ~ "December",)) %>%
  mutate(Month =factor(Month,levels = c("January","February", "March","April",
                                        "May","June","July","August","September",
                                        "October","November","December"))) %>% 
  select(unit,Year,Month,CPI) 
  Euro_CPI$CPI[Euro_CPI$CPI == ":"] <- NA
Euro_CPI_I96 <- Euro_CPI %>% filter(unit=="I96")
Euro_CPI_I15 <- Euro_CPI %>% filter(unit=="I15")
Euro_CPI_I05 <- Euro_CPI %>% filter(unit=="I05")



################################################################################
# Eurostat nezaměstnanost: https://ec.europa.eu/eurostat/databrowser/view/une_rt_m__custom_9317581/default/table?lang=en
# Sezónně očištěná data
U <- read_tsv("une_rt_m_page_tabular (1).tsv",col_names = c("freq,s_adj,age,unit,sex,geo"))
U <- U %>% separate(`freq,s_adj,age,unit,sex,geo`,
                                  c("freq","s_adj","age","unit","sex","geo","time_period"),sep = ",|\\\\"
) 

second_row <- U[1, ]
colnames(U) <- second_row
U <- U %>% filter(geo=="CZ") %>% pivot_longer(cols = -c("freq","s_adj","age","unit","sex","geo","TIME_PERIOD"),
                        names_to = "Date",
                        values_to = "urate") %>% mutate(Month=as.numeric(str_extract(Date,"[0-9]{2}$")),
                                                        Year = as.numeric(str_extract(Date,"^[0-9]{4}"))
                        ) %>% mutate(Month = case_when(Month == 01 ~ "January",
                                                       Month == 02 ~ "February",
                                                       Month == 03 ~ "March",
                                                       Month == 04 ~ "April",
                                                       Month == 05 ~ "May",
                                                       Month == 06 ~ "June",
                                                       Month == 07 ~ "July",
                                                       Month == 08 ~ "August",
                                                       Month == 09 ~ "September",
                                                       Month == 10 ~ "October",
                                                       Month == 11 ~ "November",
                                                       Month == 12 ~ "December",)) %>%
  mutate(Month =factor(Month,levels = c("January","February", "March","April",
                                        "May","June","July","August","September",
                                        "October","November","December"))) %>%
  select(Year,Month,urate)
U$urate[U$urate == ":"] <- NA

# Eurostat úrokové sazby
r = read_tsv("irt_st_m_page_tabular.tsv",col_names = c("freq,int_rt,geo"))
r <- r %>% separate(`freq,int_rt,geo`,
                    c("freq","int_rt","geo","time_period"),sep = ",|\\\\"
) 
second_row <- r[1, ]
colnames(r) <- second_row
r <- r %>% filter(geo=="CZ") %>% pivot_longer(cols = -c("freq","int_rt","geo","TIME_PERIOD"),
                                         names_to = "Date",
                                         values_to = "r") %>% mutate(Month=as.numeric(str_extract(Date,"[0-9]{2}$")),
                                                                        Year = as.numeric(str_extract(Date,"^[0-9]{4}"))
                                         )%>% mutate(Month = case_when(Month == 01 ~ "January",
                                                                                       Month == 02 ~ "February",
                                                                                       Month == 03 ~ "March",
                                                                                       Month == 04 ~ "April",
                                                                                       Month == 05 ~ "May",
                                                                                       Month == 06 ~ "June",
                                                                                       Month == 07 ~ "July",
                                                                                       Month == 08 ~ "August",
                                                                                       Month == 09 ~ "September",
                                                                                       Month == 10 ~ "October",
                                                                                       Month == 11 ~ "November",
                                                                                       Month == 12 ~ "December",)) %>%
  mutate(Month =factor(Month,levels = c("January","February", "March","April",
                                        "May","June","July","August","September",
                                        "October","November","December"))) %>%
  select(Year,Month,r)

U$urate[U$urate == ":"] <- NA
#################################################################################
# Labour cost index - EUROSTAT: https://ec.europa.eu/eurostat/databrowser/view/lc_lci_r2_q__custom_9321322/default/table?lang=en
Labour <- read_tsv("lc_lci_r2_q_page_tabular.tsv",col_names = c("freq,s_adj,unit,nace_r2,lcstruct,geo"))

Labour <- Labour %>% separate(`freq,s_adj,unit,nace_r2,lcstruct,geo`,
                    c("freq","s_adj","unit","nace_r2","lcstruct","geo","time_period"),sep = ",|\\\\"
) 

second_row <- Labour[1, ]
colnames(Labour) <- second_row
Labour <- Labour %>% filter(geo == "CZ")%>% pivot_longer(cols = -c("freq","s_adj","unit","nace_r2","lcstruct","geo","TIME_PERIOD"),
                                                         names_to = "Date",
                                                         values_to = "Labour_index")%>% 
  mutate(Quarter=str_extract(Date,"[Q][0-9]$"),
        Year = as.numeric(str_extract(Date,"^[0-9]{4}"))
                                                         ) %>%
  select(Year,Quarter,Labour_index)

  Labour$Labour_index[Labour$Labour_index == ":"] <- NA
  Labour$Labour_index <- str_extract(Labour$Labour_index,"[-]?[0-9]+[.][0-9]+")

  Data <- left_join(r, Euro_CPI_I05, by = c("Year", "Month")) %>%
arrange(Year,Month)  %>% select(Year,Month,CPI,r)
  Data <- merge(Data,U,by = c("Year","Month")) %>% arrange(Year, Month)
  
GDP <- GDP %>% fill(Year)
GDP$date <- ymd(paste(GDP$Year, GDP$Quarter, "1"))
GDP %>% ggplot(aes(y=GDP_change,x = date)) + geom_line(size = 1, color = "blue")


Debt <- read_tsv("gov_10q_ggdebt_page_tabular.tsv", col_names = c("freq,na_item,sector,unit,geo"))
Debt <- Debt %>% separate(`freq,na_item,sector,unit,geo`,
                              c("freq","na_item","sector","unit","geo","time_period"),sep = ",|\\\\"
) 

second_row <- Debt[1, ]
colnames(Debt) <- second_row
Debt <- Debt %>% filter(geo == "CZ")%>% pivot_longer(cols = -c("freq","na_item","sector","unit","geo","TIME_PERIOD"),
                                                         names_to = "Date",
                                                         values_to = "Debt")%>% 
  mutate(Quarter=str_extract(Date,"[Q][0-9]$"),
         Year = as.numeric(str_extract(Date,"^[0-9]{4}"))
  ) %>%
  select(Year,Quarter,Debt)
Debt$Debt[Debt$Debt == ":"] <- NA
Debt$Debt <- str_extract(Debt$Debt,"[-]?[0-9]+[.][0-9]+")



Quarter_Data <- left_join(GDP,Labour,by = c("Year","Quarter"))
Quarter_Data <- left_join(Quarter_Data,Debt,by = c("Year","Quarter"))
Quarter_Data <- Quarter_Data %>%
  mutate(Month = case_when(
    Quarter == "Q1" ~ "March",
    Quarter == "Q2" ~ "June",
    Quarter == "Q3" ~ "September",
    Quarter == "Q4" ~ "December",
    TRUE ~ NA_character_
  )) 
Final_data <- left_join(Data,Quarter_Data, by = c("Year","Month")) %>% 
  select(Year,Month,Quarter, GDP, GDP_change,CPI,r,urate,Labour_index,Debt)
Final_data$Year <- as.numeric(Final_data$Year)
Final_data$GDP <- as.numeric(Final_data$GDP)
Final_data$CPI <- as.numeric(Final_data$CPI)
Final_data$r <- as.numeric(Final_data$r)
Final_data$urate <- as.numeric(Final_data$urate)
Final_data$Labour_index <- as.numeric(Final_data$Labour_index)
Final_data$GDP_change <- as.numeric(Final_data$GDP_change)
Final_data$Debt <- as.numeric(Final_data$Debt)
CZ_time_series <- tibble(Year = Final_data$Year,
                         Month = Final_data$Month,
                         Quarter = Final_data$Quarter,
                         GDP = Final_data$GDP,
                         CPI = Final_data$CPI,
                         r = Final_data$r,
                         urate = Final_data$urate,
                         Labour_index = Final_data$Labour_index,
                         GDP_change = Final_data$GDP_change,
                         Debt = Final_data$Debt)
CZ_time_series <- CZ_time_series %>% mutate(Inflace = c(NA, diff(CPI, lag = 1, na.pad = FALSE)))
library(lubridate)
CZ_time_series$date <- ymd(paste(CZ_time_series$Year, CZ_time_series$Month, "1"))






# Wages: https://www.czso.cz/csu/czso/pmz_ts
Wage <- read_excel("pmzcr120423_1.xlsx", 
                            range = "A38:D196", col_names = c("Date","abs","nom","Real_wage"))
Wage <- Wage %>%
  filter((row_number() %% 7) <= 4)%>%
  filter(complete.cases(.)) %>% mutate(Quarter = str_extract(Date,"[Q][1-4]$")) %>% 
  slice(-n()) %>% mutate(Year = str_extract(Date,"^[0-9]{4}")) %>% 
  fill(Year) %>% select(Year,Quarter,Real_wage) %>% mutate(Real_wage_diff = Real_wage - lag(Real_wage)) %>% 
  mutate(Year = as.double(Year))
CZ_time_series <- left_join(CZ_time_series,Wage,by = c("Year","Quarter"))


# Rate volných pracovních míst: https://ec.europa.eu/eurostat/databrowser/view/jvs_q_nace2__custom_9428028/default/table?lang=en

Vacc <- read_tsv("jvs_q_nace2_page_tabular.tsv",col_names = c("freq,s_adj,unit,nace_r2,sizeclas,indic_em,geo"))

Vacc <- Vacc %>% separate(`freq,s_adj,unit,nace_r2,sizeclas,indic_em,geo`,
                              c("freq","s_adj","nace_r2","sizeclas","indic_em","geo","time_period"),sep = ",|\\\\"
) 

second_row <- Vacc[1, ]
colnames(Vacc) <- second_row
Vacc <- Vacc %>% filter(geo == "CZ")%>% pivot_longer(cols = -c("freq","s_adj","nace_r2","sizeclas","indic_em","geo","TIME_PERIOD"),
                                                         names_to = "Date",
                                                         values_to = "Vacc_index")%>% 
  mutate(Quarter=str_extract(Date,"[Q][0-9]$"),
         Year = as.numeric(str_extract(Date,"^[0-9]{4}"))
  ) %>%
  select(Year,Quarter,Vacc_index)

Vacc$Vacc_index[Vacc$Vacc_index== ":"] <- NA

CZ_time_series <- left_join(CZ_time_series,Vacc,by = c("Year","Quarter"))


# Effective exchange rate: Bank for International Settlements (2024), Effective exchange rates, BIS WS_EER 1.0 (data set), https://data.bis.org/topics/EER/data (accessed on 19 January 2024).
# https://data.bis.org/topics/EER/data?data_view=table&filter=FREQ%3DM%255EEER_TYPE%3DR%255EEER_BASKET%3DB%255EREF_AREA_TXT%3DCzechia%255ETIMESPAN%3D1994-01-01_2023-12-31
E_rate <- read_excel("bis_dp_search_export_20240119-134900.xlsx", 
                                                   sheet = "timeseries observations")
E_rate <- E_rate %>% select(`TIME_PERIOD:Period`,`OBS_VALUE:Value`) %>%
  mutate(Date = E_rate$`TIME_PERIOD:Period`) %>% select(Date,`OBS_VALUE:Value`) %>% 
  mutate(Year = as.numeric(str_extract(Date, "^[0-9]{4}")),
         Month = str_extract(Date,"[-][0-9]{2}[-]")) %>% mutate(Month = as.numeric(str_extract(Month,"[0-9]{2}"))) %>%
  mutate(Month = case_when(Month == 01 ~ "January",
                           Month == 02 ~ "February",
                           Month == 03 ~ "March",
                           Month == 04 ~ "April",
                           Month == 05 ~ "May",
                           Month == 06 ~ "June",
                           Month == 07 ~ "July",
                           Month == 08 ~ "August",
                           Month == 09 ~ "September",
                           Month == 10 ~ "October",
                           Month == 11 ~ "November",
                           Month == 12 ~ "December",)) %>%  mutate(E_rate = `OBS_VALUE:Value`) %>% 
  select(Year,Month,E_rate) %>% mutate(E_rate = E_rate - lag(E_rate))
CZ_time_series <- left_join(CZ_time_series,E_rate,by = c("Year","Month"))

CZ_time_series %>% ggplot(aes(y=E_rate,x = date)) + geom_line(size = 1, color = "blue")
CZ_time_series <- CZ_time_series %>% select(Year,Month,Quarter,GDP_change,r,urate,Labour_index,Inflace,Real_wage_diff,Vacc_index,E_rate,date)
CZ_time_series %>% ggplot(aes(y = Inflace,x = date)) + geom_line(size = 1, color = "blue")
CZ_time_series %>% ggplot(aes(y = urate,x = date)) + geom_line(size = 1, color = "blue")
CZ_time_series %>% ggplot(aes(y = r,x = date)) + geom_line(size = 1, color = "blue")

# Save results
save(CZ_time_series, file = "CZ_time_series.RData")
GDP$date <- ymd(paste(GDP$Year, GDP$Quarter, "1"))
library(lubridate)

# Upravený kód pro přidávání čísel 3, 6, 9 a 12
GDP$date <- ymd(sprintf("%d-%02d-01", GDP$Year, ifelse(GDP$Quarter == "Q1", 3,
                                                       ifelse(GDP$Quarter == "Q2", 6,
                                                              ifelse(GDP$Quarter == "Q3", 9, 12)))))


library(writexl)
write_xlsx(CZ_time_series, "C:/Users/cerma/OneDrive/Důležité věci/Diplomova_prace/Data_diplomka.xlsx")
write_xlsx(GDP, "C:/Users/cerma/OneDrive/Důležité věci/Diplomova_prace/GDP.xlsx")

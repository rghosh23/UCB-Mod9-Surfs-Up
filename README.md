# Temperature Trends Analysis for Oahu
## Overview of Temperature data analysis
We want to open a surf and shakes shop in Oahu, Hawaii. A serious investor, W. Avy, is interested in investing however, he is very interested in studying the temperature trends in Oahu in order to make a decision. He has asked for a temperature trends analysis. 
### Purpose
Using SQlAlchemy, temperature in June and December in Hawaii can be processed in an 'offline' database. By filtering the temperature of the months June or December, we can easily see the statistics of temperature and see if the surf and shakes shop will be a success in Hawaii.

## Results
**June temperature trends:**

![summary_df_June](https://user-images.githubusercontent.com/102441140/172955366-de26e7e3-7283-40f2-b3d3-2f64e9a398fd.png)

**December temperature trends:**

![summary_df_Dec](https://user-images.githubusercontent.com/102441140/172955485-a0107d53-7767-478e-bcaf-c02d53ebf44c.png)

***Three key differences*** in weather between June and December:
1. December mean temperature is Oahu lower than June temperatures. This is expected since December is in winter and June is in summer. However, the mean  temperatures for both seasons still stay around low to mid 70F, which is pretty ideal beach temperature still.
2. The minimum temperatures greatly vary between June (64F) and Deceember (56F). While, the minimum temperature in June remains pretty pleasant, in December, it drops to mid 50s, which might have an effect on the number of tourists in December, and therefore a possible dip in profits.
3. December has a slightly higher standard deviation than June, which means the deviation between the max and min temperatures are higher in December than in June. However, even then the standard deviations for both are between 3-4F so the difference should not be very noticeable.

## Summary
### *Results Summary*
Based on the analysis of temperature trends in June and December, we can recommend Oahu as a greatb location to open up a surf and shakes shop. While winter temperatures do drop, and temd to be more variable, overall it is not drastically different from summer temperatures. Also, the temperture drop might hinder ice cream sales, it should not have much of an effect on the surf shop sales, since even at brisk 56F temperatures, surfing is enjoable. 
### *Additional Queries*
1. We should check the trends in each station to confirm that we aren't missing any outlier with the max and min temperature data
2. We should also check the precipitation trends in June and December since rains and storms might affect the ice cream sales

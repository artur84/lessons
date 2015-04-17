package android_programming;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class WeatherDataParser {
	public static double getMaxTemperatureForDay(String weatherJsonStr, int dayIndex) 
			throws JSONException {
		System.out.println("Hola");
		System.out.println(weatherJsonStr);
		
		JSONObject weather = new JSONObject(weatherJsonStr);
		//As I understand a JSONArray is an Array of JSONObjects
		JSONArray days = weather.getJSONArray("list");
		//Then we select the desired JSONObject
		JSONObject dayInfo =days.getJSONObject(dayIndex);
		JSONObject temperatureInfo = dayInfo.getJSONObject("temp");
		System.out.println(days.toString());
		
		return temperatureInfo.getDouble("max");
	}
}

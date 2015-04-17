package android_programming;

import org.json.JSONException;

public class WeatherDataTester {

	    public static void main(String[] args) throws JSONException
	    {
	    	String weatherJsonStr="{\"cod\":\"200\",\"message\":0.003,\"city\":{\"id\":\"5375480\",\"name\":\"Mountain View\",\"coord\":{\"lon\":-122.077,\"lat\":37.4121},\"country\":\"United States of America\",\"population\":0},\"cnt\":7,\"list\":[{\"dt\":1422302400,\"temp\":{\"day\":16.54,\"min\":16.54,\"max\":16.54,\"night\":16.54,\"eve\":16.54,\"morn\":16.54},\"pressure\":994.61,\"humidity\":91,\"weather\":[{\"id\":804,\"main\":\"Clouds\",\"description\":\"overcast clouds\",\"icon\":\"04n\"}],\"speed\":0.95,\"deg\":187,\"clouds\":92},{\"dt\":1422388800,\"temp\":{\"day\":22.49,\"min\":9.99,\"max\":22.49,\"night\":9.99,\"eve\":16.65,\"morn\":15.96},\"pressure\":998.51,\"humidity\":68,\"weather\":[{\"id\":804,\"main\":\"Clouds\",\"description\":\"overcast clouds\",\"icon\":\"04d\"}],\"speed\":1.41,\"deg\":236,\"clouds\":92},{\"dt\":1422475200,\"temp\":{\"day\":19.94,\"min\":5.02,\"max\":19.94,\"night\":5.02,\"eve\":11.52,\"morn\":6.55},\"pressure\":999.58,\"humidity\":65,\"weather\":[{\"id\":800,\"main\":\"Clear\",\"description\":\"sky is clear\",\"icon\":\"02d\"}],\"speed\":1.4,\"deg\":341,\"clouds\":8},{\"dt\":1422561600,\"temp\":{\"day\":17.27,\"min\":1.56,\"max\":17.27,\"night\":1.56,\"eve\":8.19,\"morn\":3.68},\"pressure\":996.34,\"humidity\":67,\"weather\":[{\"id\":800,\"main\":\"Clear\",\"description\":\"sky is clear\",\"icon\":\"01d\"}],\"speed\":1.21,\"deg\":357,\"clouds\":0},{\"dt\":1422648000,\"temp\":{\"day\":14.19,\"min\":6.48,\"max\":19.49,\"night\":9.13,\"eve\":19.49,\"morn\":6.48},\"pressure\":1013.58,\"humidity\":0,\"weather\":[{\"id\":800,\"main\":\"Clear\",\"description\":\"sky is clear\",\"icon\":\"01d\"}],\"speed\":1.78,\"deg\":45,\"clouds\":0},{\"dt\":1422734400,\"temp\":{\"day\":13.95,\"min\":6.64,\"max\":19.07,\"night\":11.12,\"eve\":19.07,\"morn\":6.64},\"pressure\":1012.85,\"humidity\":0,\"weather\":[{\"id\":800,\"main\":\"Clear\",\"description\":\"sky is clear\",\"icon\":\"01d\"}],\"speed\":2.65,\"deg\":95,\"clouds\":0},{\"dt\":1422820800,\"temp\":{\"day\":12.81,\"min\":8.52,\"max\":17.02,\"night\":9.4,\"eve\":17.02,\"morn\":8.52},\"pressure\":1014.68,\"humidity\":0,\"weather\":[{\"id\":800,\"main\":\"Clear\",\"description\":\"sky is clear\",\"icon\":\"01d\"}],\"speed\":1.74,\"deg\":120,\"clouds\":47}]}";
	        int dayIndex =2;
	    	double maxTemp = WeatherDataParser.getMaxTemperatureForDay(weatherJsonStr, dayIndex);
	    	System.out.println("Max Temp for day "+ String.valueOf(dayIndex)+" is " + String.valueOf(maxTemp) );
	    }


}

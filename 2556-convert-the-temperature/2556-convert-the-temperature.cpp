class Solution {
public:
    vector<double> convertTemperature(double Celsius) {
        return vector<double>({Celsius + 273.15, Celsius * 1.80 + 32.00});
    }
};
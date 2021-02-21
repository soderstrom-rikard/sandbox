using System;

namespace Vattenrening
{

    public enum MotorStatus { Off, On, Error };

    public enum ValveStatus { Closed, Open, Error };

    public interface IWaterCleaningAdapter

    {

        void Initialize();

        void StartCirculationPump(int effect);

        void StopCirculationPump();

        MotorStatus GetCirculationPumpStatus();



        void OpenAirValve();

        void CloseAirValve();

        ValveStatus GetAirValveStatus();
    }

    public class WaterCleaningSimulator : IWaterCleaningAdapter
    {
        public void CloseAirValve()
        {
            throw new NotImplementedException();
        }

        public ValveStatus GetAirValveStatus()
        {
            throw new NotImplementedException();
        }

        public MotorStatus GetCirculationPumpStatus()
        {
            throw new NotImplementedException();
        }

        public void Initialize()
        {
            //    throw new NotImplementedException();
        }

        public void OpenAirValve()
        {
            throw new NotImplementedException();
        }

        public void StartCirculationPump(int effect)
        {
            throw new NotImplementedException();
        }

        public void StopCirculationPump()
        {
            throw new NotImplementedException();
        }
    }
}
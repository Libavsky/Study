using GalaSoft.MvvmLight;
using GalaSoft.MvvmLight.Command;
using System.Windows.Input;
using System.Xml;
using System.Xml.Serialization;
using System.Linq;
using System.Collections;
using System.Collections.Generic;
using System.Xml.Xsl;
using System.IO;
using System.Xml.Schema;
using System.Windows;
using System;

namespace Zadanie5.ViewModel
{
    /// <summary>
    /// I write bad code too, not perfect but working very well.
    /// Every not perfect part of code exists because of lack of time.
    /// Do not try to learn MVVM from this awesome project.
    /// </summary>
    public class MainViewModel : ViewModelBase
    {
        #region Properties
        public CarRental CarRental
        {
            get { return _carRental; }
            set
            {
                if (value != _carRental)
                {
                    _carRental = value;
                    RaisePropertyChanged("CarRental");
                }
            }
        }

        public wypo¿yczalniaUs³ugiPracownik NewEmployee
        {
            get { return _newEmployee; }
            set
            {
                if (value != _newEmployee)
                {
                    _newEmployee = value;
                    RaisePropertyChanged("NewEmployee");
                }
            }
        }

        public wypo¿yczalniaSamochód NewCar
        {
            get { return _newCar; }
            set
            {
                if (value != _newCar)
                {
                    _newCar = value;
                    RaisePropertyChanged("NewCar");
                }
            }
        }

        public wypo¿yczalniaUs³ugiWypo¿yczenie NewRental
        {
            get { return _newRental; }
            set
            {
                if (value != _newRental)
                {
                    _newRental = value;
                    RaisePropertyChanged("NewRental");
                }
            }
        }

        public List<string> AvailableCarsIdexes
        {
            get
            {
                return CarRental.samochody.Where(x => x.czy_wypo¿yczone == "nie" || x.czy_wypo¿yczone == "Nie").Select(x => x.id).ToList();
            }
        }

        public List<string> AvailableEmployeesIdexes
        {
            get
            {
                return CarRental.us³ugi.pracownicy.Select(x => x.id).ToList();
            }
        }
        public int SelectedCar
        {
            get { return _selectedCar; }
            set
            {
                if (value != _selectedCar)
                {
                    _selectedCar = value;
                    RaisePropertyChanged("SelectedCar");
                }
            }
        }

        public int SelectedRental
        {
            get { return _selectedRental; }
            set
            {
                if (value != _selectedRental)
                {
                    _selectedRental = value;
                    RaisePropertyChanged("SelectedCar");
                }
            }
        }

        public int SelectedEmployee
        {
            get { return _selectedEmployee; }
            set
            {
                if (value != _selectedEmployee)
                {
                    _selectedEmployee = value;
                    RaisePropertyChanged("SelectedCar");
                }
            }
        }
        #endregion

        #region Main
        public MainViewModel()
        {
            if (ValidateSchema("../../Documents/zadanie5.xml", "../../Documents/zadanie5.xsd"))
            {
                XmlSerializer serializer = new XmlSerializer(typeof(CarRental));
                CarRental = (CarRental)serializer.Deserialize(new XmlTextReader("../../Documents/zadanie5.xml"));
            }
            else
            {
                MessageBoxResult result = MessageBox.Show("zadanie5.xml not valid, check document and run program again\n", "Validation Error", MessageBoxButton.OK, MessageBoxImage.Error);
                if (result == MessageBoxResult.OK)
                {
                    Application.Current.Shutdown();
                }
            }

            SelectedCar = -1;
            SelectedEmployee = -1;
            SelectedRental = -1;

            NewEmployee = new wypo¿yczalniaUs³ugiPracownik();
            NewCar = new wypo¿yczalniaSamochód();
            NewCar.nazwa = new wypo¿yczalniaSamochódNazwa();
            NewRental = new wypo¿yczalniaUs³ugiWypo¿yczenie();
            NewRental.wypo¿yczaj¹cy = new wypo¿yczalniaUs³ugiWypo¿yczenieWypo¿yczaj¹cy();
        }

        #endregion

        #region Commands
        public ICommand DeleteCarCommand => _deleteCarCommand ?? (_deleteCarCommand = new RelayCommand(() =>
        {
            if (SelectedCar > -1)
                CarRental.samochody.RemoveAt(SelectedCar);
        }));

        public ICommand AddCarCommand => _addCarCommand ?? (_addCarCommand = new RelayCommand(() =>
        {
            string id = string.Empty;
            if (!string.IsNullOrEmpty(NewCar.nazwa.marka) && !string.IsNullOrEmpty(NewCar.nazwa.model))
            {
                id = NewCar.nazwa.model[0].ToString() + NewCar.nazwa.marka[0].ToString();
                int number = 0;
                do
                {
                    number++;
                } while (CarRental.samochody.Where(x => x.id == (id + number)) as wypo¿yczalniaSamochód != null);
                id = id + number;
            }

            NewCar.id = id;
            NewCar.czy_wypo¿yczone = "nie";

            CarRental.samochody.Add(NewCar);
        }));

        public ICommand DeleteRentalCommand => _deleteRentalCommand ?? (_deleteRentalCommand = new RelayCommand(() =>
        {
            if (SelectedRental > -1)
                CarRental.us³ugi.wypo¿yczenia.RemoveAt(SelectedRental);
        }));

        public ICommand AddRentalCommand => _addRentalCommand ?? (_addRentalCommand = new RelayCommand(() =>
        {
            CarRental.us³ugi.wypo¿yczenia.Add(NewRental);
        }));

        public ICommand DeleteEmployeeCommand => _deleteEmployeeCommand ?? (_deleteEmployeeCommand = new RelayCommand(() =>
        {
            if (SelectedEmployee > -1)
                CarRental.us³ugi.pracownicy.RemoveAt(SelectedEmployee);
        }));

        public ICommand AddEmployeeCommand => _addEmployeeCommand ?? (_addEmployeeCommand = new RelayCommand(() =>
        {
            string id = string.Empty;
            if (!string.IsNullOrEmpty(NewEmployee.imie) && !string.IsNullOrEmpty(NewEmployee.imie))
            {
                id = NewEmployee.imie[0].ToString() + NewEmployee.nazwisko[0].ToString();
                int number = 0;
                do
                {
                    number++;
                } while (CarRental.us³ugi.pracownicy.Where(x => x.id == (id + number)) as wypo¿yczalniaUs³ugiPracownik != null);
                id = id + number;
            }

            NewEmployee.id = id;

            CarRental.us³ugi.pracownicy.Add(NewEmployee);
        }));

        public ICommand SaveCommand => _saveCommand ?? (_saveCommand = new RelayCommand(() =>
        {
            //TODO: Saving and checking with XML Schema

            XmlSerializer serializer = new XmlSerializer(typeof(CarRental));

            using (XmlTextWriter writer = new XmlTextWriter("../../Documents/tmp.xml", System.Text.Encoding.UTF8))
            {
                serializer.Serialize(writer, CarRental);
            }

            if (ValidateSchema("../../Documents/tmp.xml", "../../Documents/zadanie5.xsd"))
            {
                File.Copy("../../Documents/tmp.xml", "../../Documents/zadanie5.xml", true);
                File.Delete("../../Documents/tmp.xml");
                MessageBox.Show("Changes saved to zadanie5.xml");
            }
            else
            {
                File.Delete("../../Documents/tmp.xml");
                MessageBox.Show("Changes not saved to zadanie5.xml, check validity");
            }
        }));

        public ICommand TransformToHTML => _transformToHTML ?? (_transformToHTML = new RelayCommand(() =>
        {

            XslCompiledTransform raportXsltTransform = new XslCompiledTransform();
            raportXsltTransform.Load("../../Documents/zadanie5.xslt", XsltSettings.TrustedXslt, new XmlUrlResolver());
            raportXsltTransform.Transform("../../Documents/zadanie5.xml", "../../Documents/zadanie5_raport.xml");

            XslCompiledTransform htmlXsltTransform = new XslCompiledTransform();
            htmlXsltTransform.Load("../../Documents/zadanie5_html.xslt");
            htmlXsltTransform.Transform("../../Documents/zadanie5_raport.xml", "../../Documents/zadanie5.html");

            //I know system specific operations should be in adapters but who cares ...
            System.Diagnostics.Process.Start(Path.GetFullPath("../../Documents/zadanie5.html"));
        }));
        #endregion

        #region Private Methods

        private bool ValidateSchema(string xmlPath, string xsdPath)
        {
            XmlDocument xml = new XmlDocument();
            xml.Load(xmlPath);

            XmlTextReader schemaReader = new XmlTextReader(xsdPath);
            XmlSchema schema = XmlSchema.Read(schemaReader, null);

            xml.Schemas.Add(schema);

            try
            {
                xml.Validate(null);
            }
            catch (XmlSchemaValidationException e)
            {
                //I know how bad it is, messagebox in catch in mvvm view model, but who cares ...
                MessageBox.Show(e.Message, "Validation Error");
                return false;
            }
            return true;
        }

        private bool ValidateSchema(XmlDocument xml, string xsdPath)
        {
            xml.Schemas.Add(null, xsdPath);

            try
            {
                xml.Validate(null);
            }
            catch (XmlSchemaValidationException)
            {
                return false;
            }
            return true;
        }
        #endregion
        
        #region Fields
        private ICommand _deleteCarCommand;
        private ICommand _addCarCommand;
        private ICommand _deleteRentalCommand;
        private ICommand _addRentalCommand;
        private ICommand _deleteEmployeeCommand;
        private ICommand _addEmployeeCommand;

        private ICommand _saveCommand;
        private ICommand _transformToHTML;

        private CarRental _carRental;
        private wypo¿yczalniaUs³ugiPracownik _newEmployee;
        private wypo¿yczalniaSamochód _newCar;
        private wypo¿yczalniaUs³ugiWypo¿yczenie _newRental;

        private int _selectedCar;
        private int _selectedRental;
        private int _selectedEmployee;
        #endregion
    }
}
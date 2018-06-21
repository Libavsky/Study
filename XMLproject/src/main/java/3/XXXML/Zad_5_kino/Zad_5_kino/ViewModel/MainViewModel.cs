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
using Zad_5_kino.Model;


namespace Zad_5_kino.ViewModel
{
    /// <summary>
    /// This class contains properties that the main View can data bind to.
    /// <para>
    /// Use the <strong>mvvminpc</strong> snippet to add bindable properties to this ViewModel.
    /// </para>
    /// <para>
    /// You can also use Blend to data bind with the tool's support.
    /// </para>
    /// <para>
    /// See http://www.galasoft.ch/mvvm
    /// </para>
    /// </summary>
    public class MainViewModel : ViewModelBase
    {
        /// <summary>
         #region Properties
        public repertuar repertuar
        {
            get { return _repertuar; }
            set
            {
                if (value != _repertuar)
                {
                    _repertuar = value;
                    RaisePropertyChanged("repertuar");
                }
            }
        }

        public repertuarWyœwietlanieSeans NewSeans
        {
            get { return _newSeans; }
            set
            {
                if (value != _newSeans)
                {
                    _newSeans = value;
                    RaisePropertyChanged("NewSeans");
                }
            }
        }

        public repertuarFilm NewFilm
        {
            get { return _newFilm; }
            set
            {
                if (value != _newFilm)
                {
                    _newFilm = value;
                    RaisePropertyChanged("NewFilm");
                }
            }
        }

        public repertuarWyœwietlanieKino NewKino
        {
            get { return _newKino; }
            set
            {
                if (value != _newKino)
                {
                    _newKino = value;
                    RaisePropertyChanged("NewKino");
                }
            }
        }
        public int SelectedFilm
        {
            get { return _selectedFilm; }
            set
            {
                if (value != _selectedFilm)
                {
                    _selectedFilm = value;
                    RaisePropertyChanged("SelectedFilm");
                }
            }
        }

        public int SelectedSeans
        {
            get { return _selectedSeans; }
            set
            {
                if (value != _selectedSeans)
                {
                    _selectedSeans = value;
                    RaisePropertyChanged("SelectedSeans");
                }
            }
        }

        public int SelectedKino
        {
            get { return _selectedKino; }
            set
            {
                if (value != _selectedKino)
                {
                    _selectedKino = value;
                    RaisePropertyChanged("SelectedKino");
                }
            }
        }
        #endregion

        #region Main
        public MainViewModel()
        {
            if (ValidateSchema("../../Document/filmy.xml", "../../Document/movies.xsd"))
            {
                XmlSerializer serializer = new XmlSerializer(typeof(repertuar));
                repertuar = (repertuar)serializer.Deserialize(new XmlTextReader("../../Document/filmy.xml"));
            }
            else
            {
                MessageBoxResult result = MessageBox.Show("film.xml not valid, check document and run program again\n", "Validation Error", MessageBoxButton.OK, MessageBoxImage.Error);
                if (result == MessageBoxResult.OK)
                {
                    Application.Current.Shutdown();
                }
            }

            SelectedFilm = -1;
            SelectedSeans = -1;
            SelectedKino = -1;

            NewSeans = new repertuarWyœwietlanieSeans();
            NewFilm = new repertuarFilm();
            NewFilm.ograniczenie_wiekowe = new repertuarFilmOgraniczenie_wiekowe();
            NewFilm.gatunek = new repertuarFilmGatunek();
            NewFilm.box_office = new repertuarFilmBox_office();
            NewKino = new repertuarWyœwietlanieKino();
                
        }

        #endregion

        #region Commands
        public ICommand DeleteFilmCommand => _deleteFilmCommand ?? (_deleteFilmCommand = new RelayCommand(() =>
        {
            if (SelectedFilm > -1)
                repertuar.filmy.RemoveAt(SelectedFilm);
        }));

        public ICommand AddFilmCommand => _addFilmCommand ?? (_addFilmCommand = new RelayCommand(() =>
        {
            string id = string.Empty;
            if (!string.IsNullOrEmpty(NewFilm.tytu³) && !string.IsNullOrEmpty(NewFilm.tytu³))
            {
                id = NewFilm.id.ToString();
                int number = 0;
                do
                {
                    number++;
                } while (repertuar.filmy.Where(x => x.id == (id + number)) as repertuarFilm != null);
                id = id + number;
            }

            NewFilm.id = id;
            repertuar.filmy.Add(NewFilm);
        }));

        public ICommand DeleteKinoCommand => _deleteKinoCommand ?? (_deleteKinoCommand = new RelayCommand(() =>
        {
            if (SelectedKino > -1)
                repertuar.wyœwietlanie.kina.RemoveAt(SelectedKino);
        }));

        public ICommand AddKinoCommand => _addKinoCommand ?? (_addKinoCommand = new RelayCommand(() =>
        {
            repertuar.wyœwietlanie.kina.Add(NewKino);
        }));

        public ICommand DeleteSeansCommand => _deleteSeansCommand ?? (_deleteSeansCommand = new RelayCommand(() =>
        {
            if (SelectedSeans > -1)
                repertuar.wyœwietlanie.seanse.RemoveAt(SelectedSeans);
        }));

        public ICommand AddSeansCommand => _addSeansCommand ?? (_addSeansCommand = new RelayCommand(() =>
        {

            repertuar.wyœwietlanie.seanse.Add(NewSeans);
        }));

        public ICommand SaveCommand => _saveCommand ?? (_saveCommand = new RelayCommand(() =>
        {
            //TODO: Saving and checking with XML Schema

            XmlSerializer serializer = new XmlSerializer(typeof(repertuar));

            using (XmlTextWriter writer = new XmlTextWriter("../../Document/tmp.xml", System.Text.Encoding.UTF8))
            {
                serializer.Serialize(writer, repertuar);
            }

            if (ValidateSchema("../../Document/tmp.xml", "../../Document/movies.xsd"))
            {
                File.Copy("../../Document/tmp.xml", "../../Document/zadanie5.xml", true);
                File.Delete("../../Document/tmp.xml");
                MessageBox.Show("Changes saved to zadanie5.xml");
            }
            else
            {
                File.Delete("../../Document/tmp.xml");
                MessageBox.Show("Changes not saved to zadanie5.xml, check validity");
            }
        }));

        public ICommand TransformToHTML => _transformToHTML ?? (_transformToHTML = new RelayCommand(() =>
        {

            XslCompiledTransform raportXsltTransform = new XslCompiledTransform();
            raportXsltTransform.Load("../../Document/film_pomocniczy.xslt", XsltSettings.TrustedXslt, new XmlUrlResolver());
            raportXsltTransform.Transform("../../Document/zadanie5.xml", "../../Document/zadanie5_raport.xml");

            XslCompiledTransform htmlXsltTransform = new XslCompiledTransform();
            htmlXsltTransform.Load("../../Document/film_to_html.xslt");
            htmlXsltTransform.Transform("../../Document/zadanie5_raport.xml", "../../Document/zadanie5.html");

            //I know system specific operations should be in adapters but who cares ...
            System.Diagnostics.Process.Start(Path.GetFullPath("../../Document/zadanie5.html"));
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
        private ICommand _deleteFilmCommand;
        private ICommand _addFilmCommand;
        private ICommand _deleteSeansCommand;
        private ICommand _addSeansCommand;
        private ICommand _deleteKinoCommand;
        private ICommand _addKinoCommand;

        private ICommand _saveCommand;
        private ICommand _transformToHTML;

        private repertuar _repertuar;
        private repertuarFilm _newFilm;
        private repertuarWyœwietlanieKino _newKino;
        private repertuarWyœwietlanieSeans _newSeans;
       

        private int _selectedFilm;
        private int _selectedKino;
        private int _selectedSeans;
        #endregion
    }
}
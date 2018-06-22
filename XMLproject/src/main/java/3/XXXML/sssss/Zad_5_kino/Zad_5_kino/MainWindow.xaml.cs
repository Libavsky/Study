using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Zad_5_kino.Views;
using Zad_5_kino.ViewModel;

namespace Zad_5_kino
{
    /// <summary>
    /// Logika interakcji dla klasy MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private MainViewModel _vm;
        public MainWindow()
        {
            InitializeComponent();
            filmFrame.Navigate(new WyswietlFilmy());
            kinoFrame.Navigate(new WyswietlKina());
            seansFrame.Navigate(new WyswietlSeanse());

            Loaded += MainWindow_Loaded;
        }
        private void MainWindow_Loaded(object sender, RoutedEventArgs e)
        {
            _vm = DataContext as MainViewModel;
        }
        private void DeleteFilm(object sender, RoutedEventArgs e)
        {
            _vm.DeleteFilmCommand.Execute(null);
        }

        private void DeleteKino(object sender, RoutedEventArgs e)
        {
            _vm.DeleteKinoCommand.Execute(null);
        }

        private void DeleteSeans(object sender, RoutedEventArgs e)
        {
            _vm.DeleteSeansCommand.Execute(null);
        }

        private void AddFilm(object sender, RoutedEventArgs e)
        {
            filmFrame.Navigate(new DodajFilm());
        }

        private void AddKino(object sender, RoutedEventArgs e)
        {
            kinoFrame.Navigate(new DodajKina());
        }

        private void AddSeans(object sender, RoutedEventArgs e)
        {
            seansFrame.Navigate(new DodajSeans());
        }

        private void ConfirmFilm(object sender, RoutedEventArgs e)
        {
            _vm.AddFilmCommand.Execute(null);
            filmFrame.GoBack();
        }

        private void ConfirmKino(object sender, RoutedEventArgs e)
        {
            _vm.AddKinoCommand.Execute(null);
            kinoFrame.GoBack();
        }

        private void ConfirmSeans(object sender, RoutedEventArgs e)
        {
            _vm.AddSeansCommand.Execute(null);
            seansFrame.GoBack();
        }

        private void filmFrame_Navigated(object sender, NavigationEventArgs e)
        {

        }
    }
}

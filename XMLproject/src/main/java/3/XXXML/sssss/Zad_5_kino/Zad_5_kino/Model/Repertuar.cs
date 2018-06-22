using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Zad_5_kino.Model
{
    /// <remarks/>
    [System.SerializableAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
    [System.Xml.Serialization.XmlRootAttribute(Namespace = "", IsNullable = false)]
    public partial class repertuar
    {

        private repertuarMetadane metadaneField;

        private ObservableCollection<repertuarFilm> filmyField;

        private repertuarStudio[] studiaField;

        private repertuarWyświetlanie wyświetlanieField;

        /// <remarks/>
        public repertuarMetadane metadane
        {
            get
            {
                return this.metadaneField;
            }
            set
            {
                this.metadaneField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlArrayItemAttribute("film", IsNullable = false)]
        public ObservableCollection<repertuarFilm>  filmy
        {
            get
            {
                return this.filmyField;
            }
            set
            {
                this.filmyField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlArrayItemAttribute("studio", IsNullable = false)]
        public repertuarStudio[] studia
        {
            get
            {
                return this.studiaField;
            }
            set
            {
                this.studiaField = value;
            }
        }

        /// <remarks/>
        public repertuarWyświetlanie wyświetlanie
        {
            get
            {
                return this.wyświetlanieField;
            }
            set
            {
                this.wyświetlanieField = value;
            }
        }
    }

    /// <remarks/>
    [System.SerializableAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
    public partial class repertuarMetadane
    {

        private repertuarMetadaneAutor[] autorzyField;

        private decimal wersjaField;

        private string opisField;

        /// <remarks/>
        [System.Xml.Serialization.XmlArrayItemAttribute("autor", IsNullable = false)]
        public repertuarMetadaneAutor[] autorzy
        {
            get
            {
                return this.autorzyField;
            }
            set
            {
                this.autorzyField = value;
            }
        }

        /// <remarks/>
        public decimal wersja
        {
            get
            {
                return this.wersjaField;
            }
            set
            {
                this.wersjaField = value;
            }
        }

        /// <remarks/>
        public string opis
        {
            get
            {
                return this.opisField;
            }
            set
            {
                this.opisField = value;
            }
        }
    }

    /// <remarks/>
    [System.SerializableAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
    public partial class repertuarMetadaneAutor
    {

        private string imieField;

        private string nazwiskoField;

        /// <remarks/>
        [System.Xml.Serialization.XmlAttributeAttribute()]
        public string imie
        {
            get
            {
                return this.imieField;
            }
            set
            {
                this.imieField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlAttributeAttribute()]
        public string nazwisko
        {
            get
            {
                return this.nazwiskoField;
            }
            set
            {
                this.nazwiskoField = value;
            }
        }
    }

    /// <remarks/>
    [System.SerializableAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
    public partial class repertuarFilm
    {

        private string tytułField;

        private string[] reżyserField = { "sdd" };

        private System.DateTime data_premieryField;

        private repertuarFilmAktor[] aktorzyField = {new repertuarFilmAktor() };

        private repertuarFilmGatunek gatunekField;

        private repertuarFilmBox_office box_officeField;

        private repertuarFilmOgraniczenie_wiekowe ograniczenie_wiekoweField;

        private byte ocenaField;

        private string idField;

        private string studioField;

        /// <remarks/>
        public string tytuł
        {
            get
            {
                return this.tytułField;
            }
            set
            {
                this.tytułField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute("reżyser")]
        public string[] reżyser
        {
            get
            {
                return this.reżyserField;
            }
            set
            {
                this.reżyserField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(DataType = "date")]
        public System.DateTime data_premiery
        {
            get
            {
                return this.data_premieryField;
            }
            set
            {
                this.data_premieryField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlArrayItemAttribute("aktor", IsNullable = false)]
        public repertuarFilmAktor[] aktorzy
        {
            get
            {
                return this.aktorzyField;
            }
            set
            {
                this.aktorzyField = value;
            }
        }

        /// <remarks/>
        public repertuarFilmGatunek gatunek
        {
            get
            {
                return this.gatunekField;
            }
            set
            {
                this.gatunekField = value;
            }
        }

        /// <remarks/>
        public repertuarFilmBox_office box_office
        {
            get
            {
                return this.box_officeField;
            }
            set
            {
                this.box_officeField = value;
            }
        }

        /// <remarks/>
        public repertuarFilmOgraniczenie_wiekowe ograniczenie_wiekowe
        {
            get
            {
                return this.ograniczenie_wiekoweField;
            }
            set
            {
                this.ograniczenie_wiekoweField = value;
            }
        }

        /// <remarks/>
        public byte ocena
        {
            get
            {
                return this.ocenaField;
            }
            set
            {
                this.ocenaField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlAttributeAttribute()]
        public string id
        {
            get
            {
                return this.idField;
            }
            set
            {
                this.idField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlAttributeAttribute()]
        public string studio
        {
            get
            {
                return this.studioField;
            }
            set
            {
                this.studioField = value;
            }
        }
    }

    /// <remarks/>
    [System.SerializableAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
    public partial class repertuarFilmAktor
    {

        private string imięField;

        private string nazwiskoField;

        private string filmwebField;

        /// <remarks/>
        public string imię
        {
            get
            {
                return this.imięField;
            }
            set
            {
                this.imięField = value;
            }
        }

        /// <remarks/>
        public string nazwisko
        {
            get
            {
                return this.nazwiskoField;
            }
            set
            {
                this.nazwiskoField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlAttributeAttribute()]
        public string filmweb
        {
            get
            {
                return this.filmwebField;
            }
            set
            {
                this.filmwebField = value;
            }
        }
    }

    /// <remarks/>
    [System.SerializableAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
    public partial class repertuarFilmGatunek
    {

        private string rodzajField;

        /// <remarks/>
        [System.Xml.Serialization.XmlAttributeAttribute()]
        public string rodzaj
        {
            get
            {
                return this.rodzajField;
            }
            set
            {
                this.rodzajField = value;
            }
        }
    }

    /// <remarks/>
    [System.SerializableAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
    public partial class repertuarFilmBox_office
    {

        private string walutaField;

        private uint valueField;

        /// <remarks/>
        [System.Xml.Serialization.XmlAttributeAttribute()]
        public string waluta
        {
            get
            {
                return this.walutaField;
            }
            set
            {
                this.walutaField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlTextAttribute()]
        public uint Value
        {
            get
            {
                return this.valueField;
            }
            set
            {
                this.valueField = value;
            }
        }
    }

    /// <remarks/>
    [System.SerializableAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
    public partial class repertuarFilmOgraniczenie_wiekowe
    {

        private byte od_latField;

        /// <remarks/>
        [System.Xml.Serialization.XmlAttributeAttribute()]
        public byte od_lat
        {
            get
            {
                return this.od_latField;
            }
            set
            {
                this.od_latField = value;
            }
        }
    }

    /// <remarks/>
    [System.SerializableAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
    public partial class repertuarStudio
    {

        private string identyfikatorField;

        private string valueField;

        /// <remarks/>
        [System.Xml.Serialization.XmlAttributeAttribute()]
        public string identyfikator
        {
            get
            {
                return this.identyfikatorField;
            }
            set
            {
                this.identyfikatorField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlTextAttribute()]
        public string Value
        {
            get
            {
                return this.valueField;
            }
            set
            {
                this.valueField = value;
            }
        }
    }

    /// <remarks/>
    [System.SerializableAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
    public partial class repertuarWyświetlanie
    {

        private ObservableCollection<repertuarWyświetlanieKino> kinaField;

        private ObservableCollection<repertuarWyświetlanieSeans> seanseField;

        /// <remarks/>
        [System.Xml.Serialization.XmlArrayItemAttribute("kino", IsNullable = false)]
        public ObservableCollection<repertuarWyświetlanieKino> kina
        {
            get
            {
                return this.kinaField;
            }
            set
            {
                this.kinaField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlArrayItemAttribute("seans", IsNullable = false)]
        public ObservableCollection<repertuarWyświetlanieSeans> seanse
        {
            get
            {
                return this.seanseField;
            }
            set
            {
                this.seanseField = value;
            }
        }
    }

    /// <remarks/>
    [System.SerializableAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
    public partial class repertuarWyświetlanieKino
    {

        private string nazwaField;

        private string miastoField;

        private string idField;

        /// <remarks/>
        public string nazwa
        {
            get
            {
                return this.nazwaField;
            }
            set
            {
                this.nazwaField = value;
            }
        }

        /// <remarks/>
        public string miasto
        {
            get
            {
                return this.miastoField;
            }
            set
            {
                this.miastoField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlAttributeAttribute()]
        public string id
        {
            get
            {
                return this.idField;
            }
            set
            {
                this.idField = value;
            }
        }
    }

    /// <remarks/>
    [System.SerializableAttribute()]
    [System.ComponentModel.DesignerCategoryAttribute("code")]
    [System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
    public partial class repertuarWyświetlanieSeans
    {

        private System.DateTime data_seansuField;

        private string id_kinaField;

        private string id_filmuField;

        /// <remarks/>
        [System.Xml.Serialization.XmlElementAttribute(DataType = "date")]
        public System.DateTime data_seansu
        {
            get
            {
                return this.data_seansuField;
            }
            set
            {
                this.data_seansuField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlAttributeAttribute()]
        public string id_kina
        {
            get
            {
                return this.id_kinaField;
            }
            set
            {
                this.id_kinaField = value;
            }
        }

        /// <remarks/>
        [System.Xml.Serialization.XmlAttributeAttribute()]
        public string id_filmu
        {
            get
            {
                return this.id_filmuField;
            }
            set
            {
                this.id_filmuField = value;
            }
        }
    }


}

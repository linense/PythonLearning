using Microsoft.VisualStudio.TestTools.UnitTesting;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace SeleniumTests {
    [TestClass]
    public class UnitTest1 {
        [TestMethod]
        public void TestGoogleSearch() {
            IWebDriver driver = new ChromeDriver();
            driver.Navigate().GoToUrl("https://www.google.com");
            Assert.IsTrue(driver.Title.Contains("Google"));
            driver.Quit();
        }
    }
}

library(shiny)
library(shinydashboard)
library(ggplot2)
library(scales)
library(lubridate)

boardingdiff <- read.csv('boardingdiff.csv')

ui <- dashboardPage(
  dashboardHeader(title="WMATA Wait"),
  dashboardSidebar(
    sidebarMenu(
      menuItem('General Info', tabName='GI'),
      menuItem('Station Specific', tabName='SS')
    )
  ),
  dashboardBody(
    tabItems(
      tabItem(tabName = 'GI',
        dataTableOutput('alldata')
        
      ),
      tabItem(tabName = 'SS',
        sidebarLayout(
          sidebarPanel(width=3, fixed=T,
            selectInput('line', 'Select Line:', as.character(boardingdiff$Line)),
            selectInput('location', 'Select Station:', as.character(boardingdiff$LocationName)),
            selectInput('direction', 'Select Direction:', as.character(boardingdiff$Group))
          ),
          mainPanel(
            dataTableOutput('selectedline')
          )
        )
      )
    )
  )
)

stationstats <- aggregate(timediff~Line+LocationName, data=boardingdiff, FUN=mean)
linestats <- aggregate(timediff~Line, data=boardingdiff, FUN=mean)

server <- function(input, output) {
  output$alldata <- renderDataTable(stationstats[order(-stationstats$timediff),])
  
  output$selectedline <- renderDataTable({
    ss <- stationstats[which(stationstats$Line==input$line & stationstats$LocationName==input$location),]
    ss <- ss[order(-ss$timediff),]
    return(ss)
  })
}

shinyApp(ui, server)










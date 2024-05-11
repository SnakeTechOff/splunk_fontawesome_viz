# Font Awesome Visualization

## Description

The application is a fork of the **Status Indicator - Custom Visualization** application (https://splunkbase.splunk.com/app/3119) and a partial reworking of a dashboard from the **Pictorial Chart Viz** application (https://splunkbase.splunk.com/app/4687). The Font Awesome version has been updated with the latest version of the free icons.

For the moment, only one output is displayed. The output is a Font Awesome icon with a color and a text. The icon is displayed in the center of the output.

## Update of Font Awesome

If you need to update your Font Awesome version, you can replace the contents of the directory `apps/splunk_fontawesome_viz/appserver/static/fontawesome` with your own.

To update the available icon dashboard, simply run the python script `bin/html_gen.py`. Don't forget to install the modules required for the script to work properly.

```python
pip install -r requirements.txt
```

```python
python bin/html_gen.py
```

## Sample Searches

```spl
| makeresults 
| eval value = "Search" | eval icon = "magnifying-glass" | eval color = "#FF00FF" 
| table value icon color
```

## Data Format

value, icon, color, style

## Version

Version of FontAwesome used: free v6.5.2

Version of Bootstrap used: v5.3.3
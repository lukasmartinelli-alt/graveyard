package org.syncany.android;

import android.content.Context;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class MainActivity extends ActionBarActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        ArrayList<FileInfo> sampleData = new ArrayList<>();
        sampleData.add(new FileInfo("bewerbung"));
        sampleData.add(new FileInfo("Businessplan"));
        sampleData.add(new FileInfo("hsr"));
        sampleData.add(new FileInfo("rechnungen"));

        ListView fileListView = (ListView) findViewById(R.id.files_list);
        FileListAdapter fileAdapter = new FileListAdapter(this, R.layout.list_row_layout, sampleData);
        fileListView.setAdapter(fileAdapter);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    private class FileListAdapter extends ArrayAdapter<FileInfo> {

        public FileListAdapter(Context context, int resource, List<FileInfo> objects) {
            super(context, resource, objects);
        }

        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            if(convertView == null){
                convertView = View.inflate(getContext(), R.layout.list_row_layout, null);
            }
            FileInfo info = getItem(position);
            TextView nameView = (TextView) convertView.findViewById(R.id.fileName);
            nameView.setText(info.name);

            return convertView;
        }
    }
}
